"""Altair (Vega-Lite) figures from coded/*.json: per-item strategy histograms and element-reference distributions.

Run from repo root:  python3 ops_elements/figures.py
Writes ops_elements/figures/{strategies,elements,elements_heatmap,op_distribution,element_distribution}.{html,png,svg}
"""
import collections
import glob
import json
import os
import re

import altair as alt
import pandas as pd

from aggregate import EL_FAMILY, OP_ALIAS, OP_FAMILY, family, kind, ops_of

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")

INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df"
ACC_DOMAIN, ACC_RANGE = ["correct", "incorrect", "unscored"], ["#2a78d6", "#eb6834", "#c3c2b7"]
SRC_DOMAIN, SRC_RANGE = ["text only", "text + sketch", "sketch only"], ["#2a78d6", "#1baf7a", "#eb6834"]
SEQ = ["#fcfcfb", "#cde2fb", "#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]
FAM_RANGE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
CHART_ORDER = ["SB", "SB100", "SA", "AC", "AC2", "LC", "BC", "HC", "HC2", "PC", "TM", "CC", "SP", "BuC"]
STEP = 13  # px per bar row


def load():
    items = {}
    for f in sorted(glob.glob(os.path.join(HERE, "coded", "*.json"))):
        items.update(json.load(open(f)))
    meta = json.load(open(os.path.join(HERE, "items_meta.json")))
    order = sorted(items, key=lambda q: (CHART_ORDER.index(meta[q]["chart"]), q))
    return items, meta, order


def short_label(chain, vocab):
    """'FIND(x) → PROJ(...) ?wrong:read-top' -> 'FIND→PROJ ✗ read-top'."""
    ops = [OP_ALIAS.get(o, o) for o in re.findall(r"\b([A-Z][A-Za-z/]*)\b", chain) if o in vocab]
    seq = [o for i, o in enumerate(ops) if o != "ANSWER" and (i == 0 or ops[i - 1] != o)]
    lab = "→".join(seq[:6]) + ("…" if len(seq) > 6 else "") or "∅"
    m = re.search(r"\?wrong:([^\s\)\]→]+)", chain)
    if m:
        tag = m.group(1)
        lab += " ✗ " + (tag[:34] + "…" if len(tag) > 35 else tag)
    return lab


def title(q, meta, n):
    return alt.TitleParams(f"{q} · {meta[q]['chart_type']} · {meta[q]['task'].replace('_', ' ')} (n={n})",
                           anchor="start", fontSize=11, color=INK)


def strategy_rows(items, meta, order):
    vocab = {o for it in items.values() for t in it["trials"] for o in t["ops"]} | set(OP_ALIAS)
    rows = []
    for q in order:
        it = items[q]
        acc = {t["trial_id"]: t["accuracy"] for t in it["trials"]}
        for i, s in enumerate(sorted(it["strategies"], key=lambda s: -s["n"]), 1):
            a = [acc.get(t) for t in s.get("trial_ids", [])] or [None] * s["n"]
            c = collections.Counter("correct" if x == 1 else "incorrect" if x == 0 else "unscored" for x in a)
            for cls in ACC_DOMAIN:
                if c[cls]:
                    rows.append(dict(qid=q, rank=i, label=f"S{i} {short_label(s['chain'], vocab)}", accuracy=cls,
                                     trials=c[cls], total=len(a), chain=s["chain"], quote=s.get("quote", "")))
    return pd.DataFrame(rows)


def strategies_fig(items, meta, order):
    df = strategy_rows(items, meta, order)
    color = alt.Color("accuracy:N", scale=alt.Scale(domain=ACC_DOMAIN, range=ACC_RANGE),
                      legend=alt.Legend(title=None, orient="top", direction="horizontal"))
    panels = []
    for q in order:
        d = df[df.qid == q]
        y = alt.Y("label:N", sort=list(d.sort_values("rank").label.unique()), title=None,
                  axis=alt.Axis(labelLimit=360, labelFontSize=10))
        top = int(d.groupby("rank").trials.sum().max())
        step = next(k for k in (1, 2, 5, 10) if top / k <= 6)
        base = alt.Chart(d).encode(y=y)
        bars = base.mark_bar(height={"band": 0.75}, stroke="white", strokeWidth=0.6).encode(
            x=alt.X("sum(trials):Q", title=None, stack="zero", scale=alt.Scale(domain=[0, top * 1.12]),
                      axis=alt.Axis(values=list(range(0, top + 1, step)), format="d", grid=True)),
            color=color, order=alt.Order("accuracy:N"),
            tooltip=[alt.Tooltip("label:N", title="strategy"), "accuracy:N", "trials:Q",
                     alt.Tooltip("chain:N", title="full chain"), alt.Tooltip("quote:N", title="example")])
        tot = base.transform_aggregate(n="sum(trials)", groupby=["label", "rank"]).mark_text(
            align="left", dx=3, fontSize=9, color=INK2).encode(x="n:Q", text="n:Q")
        panels.append((bars + tot).properties(width=200, height=alt.Step(STEP),
                                              title=title(q, meta, len(items[q]["trials"]))))
    chart = alt.concat(*panels, columns=3, spacing=24).properties(
        title=alt.TitleParams("Strategies per item: operation chains merged up to values; bar = trials, split by accuracy",
                              subtitle="S# matches the strategy order in items.md. Hover a bar for the full chain and an example quote.",
                              anchor="start", fontSize=15))
    save(configure(chart), "strategies")


def element_rows(items, order):
    rows = []
    for q in order:
        n = len(items[q]["trials"])
        cnt = collections.defaultdict(lambda: collections.Counter())
        for t in items[q]["trials"]:
            tx = {kind(e) for e in t["elements_text"]}
            sk = {kind(e) for e in t["elements_sketch"]}
            for k in tx | sk:
                cnt[k]["text only" if k not in sk else "text + sketch" if k in tx else "sketch only"] += 1
        for k, c in cnt.items():
            for src, v in c.items():
                rows.append(dict(qid=q, element=k, source=src, trials=v, pct=100 * v / n, n=n,
                                 any_pct=100 * sum(c.values()) / n,
                                 text_pct=100 * (c["text only"] + c["text + sketch"]) / n,
                                 sketch_pct=100 * (c["sketch only"] + c["text + sketch"]) / n))
    return pd.DataFrame(rows)


def elements_fig(items, meta, order, top=10):
    df = element_rows(items, order)
    color = alt.Color("source:N", scale=alt.Scale(domain=SRC_DOMAIN, range=SRC_RANGE),
                      legend=alt.Legend(title=None, orient="top", direction="horizontal"))
    panels = []
    for q in order:
        d = df[df.qid == q]
        keep = d.groupby("element").any_pct.first().sort_values(ascending=False).index[:top]
        d = d[d.element.isin(keep)]
        bars = alt.Chart(d).mark_bar(height={"band": 0.75}, stroke="white", strokeWidth=0.6).encode(
            y=alt.Y("element:N", sort=list(keep), title=None,
                    axis=alt.Axis(labelFontSize=10)),
            x=alt.X("sum(pct):Q", title=None, scale=alt.Scale(domain=[0, 100]),
                    axis=alt.Axis(values=[0, 50, 100], labelExpr="datum.value + '%'")),
            color=color, order=alt.Order("source_order:Q"),
            tooltip=["element:N", "source:N", "trials:Q", alt.Tooltip("pct:Q", format=".0f", title="% of trials"),
                     alt.Tooltip("text_pct:Q", format=".0f", title="% in text"),
                     alt.Tooltip("sketch_pct:Q", format=".0f", title="% in sketch")],
        ).transform_calculate(source_order=f"indexof({json.dumps(SRC_DOMAIN)}, datum.source)")
        panels.append(bars.properties(width=150, height=alt.Step(STEP), title=title(q, meta, len(items[q]["trials"]))))
    chart = alt.concat(*panels, columns=4, spacing=24).properties(
        title=alt.TitleParams("Element references per item: % of trials referencing each element kind",
                              subtitle=f"Top {top} kinds per item. A trial counts once per kind, split by where it was referenced.",
                              anchor="start", fontSize=15))
    save(configure(chart), "elements")


def heatmap_fig(items, meta, order, min_total=10):
    df = element_rows(items, order)
    tot = df.groupby("element").trials.sum()
    kinds = [k for k in tot.sort_values(ascending=False).index if tot[k] >= min_total]
    cell = df[df.element.isin(kinds)].groupby(["qid", "element"]).first().reset_index()
    long = pd.concat([cell.assign(where="mentioned in text", value=cell.text_pct),
                      cell.assign(where="marked in sketch", value=cell.sketch_pct)])
    long["item"] = long.qid + " (" + long.qid.map(lambda q: meta[q]["task"].replace("_", " ")) + ")"
    long["chart_type"] = long.qid.map(lambda q: meta[q]["chart_type"])
    item_order = [f"{q} ({meta[q]['task'].replace('_', ' ')})" for q in order]
    base = alt.Chart().encode(
        x=alt.X("element:N", sort=kinds, title=None, axis=alt.Axis(labelAngle=-50, orient="top")),
        y=alt.Y("item:N", sort=item_order, title=None, axis=alt.Axis(labelFontSize=10)))
    rect = base.mark_rect(stroke="white", strokeWidth=1).encode(
        color=alt.Color("value:Q", title="% of trials", scale=alt.Scale(domain=[0, 100], range=SEQ)),
        tooltip=["item:N", "chart_type:N", "element:N", "where:N", alt.Tooltip("value:Q", format=".0f")])
    txt = base.mark_text(fontSize=8).encode(
        text=alt.Text("value:Q", format=".0f"),
        color=alt.condition("datum.value > 55", alt.value("white"), alt.value(INK))
    ).transform_filter("datum.value >= 5")
    chart = alt.layer(rect, txt).properties(width=alt.Step(26), height=alt.Step(15)).facet(
        column=alt.Column("where:N", title=None, sort=["mentioned in text", "marked in sketch"],
                          header=alt.Header(labelFontSize=13, labelFontWeight="bold", labelAnchor="start")),
        data=long).properties(
        title=alt.TitleParams("Element references by item (rows grouped by chart type)", anchor="start", fontSize=15))
    save(configure(chart), "elements_heatmap")


def distribution_fig(items, meta, order, what, min_total=3):
    """x = every operation (or element kind), grouped by family; one facet per item; y = # comments using it."""
    fams = list(OP_FAMILY if what == "ops" else EL_FAMILY)
    fam_of = lambda k: family(k, OP_FAMILY if what == "ops" else EL_FAMILY)
    per_trial = {q: [set(ops_of(t)) if what == "ops" else {kind(e) for e in t["elements_text"] + t["elements_sketch"]}
                     for t in items[q]["trials"]] for q in order}
    tot = collections.Counter(k for q in order for ks in per_trial[q] for k in ks)
    keys = [k for k in tot if tot[k] >= min_total and fam_of(k) != "other"]
    fams = [f for f in fams if f != "sketch-only"]  # rare drawing gestures fold into "other"; ≤8 colour slots
    fam_shown = lambda k: fam_of(k) if fam_of(k) in fams else "other"
    order_fams = [f for f in (OP_FAMILY if what == "ops" else EL_FAMILY) if f in fams] + ["other"]
    keys = sorted(keys, key=lambda k: (order_fams.index(fam_shown(k)), -tot[k]))
    rows = []
    for q in order:
        n = len(per_trial[q])
        c = collections.Counter(k for ks in per_trial[q] for k in ks)
        lab = f"{q} · {meta[q]['chart_type']} · {meta[q]['task'].replace('_', ' ')} (n={n})"
        for k in keys:
            rows.append(dict(item=lab, key=k, family=fam_shown(k), comments=c[k], pct=100 * c[k] / n, n=n))
    df = pd.DataFrame(rows)
    noun = "operation" if what == "ops" else "element kind"
    chart = alt.Chart(df).mark_bar(width={"band": 0.8}, cornerRadiusTopLeft=1.5, cornerRadiusTopRight=1.5).encode(
        x=alt.X("key:N", sort=keys, title=None,
                axis=alt.Axis(labelAngle=-90, labelFontSize=8, labelPadding=2, ticks=False)),
        y=alt.Y("comments:Q", title=None, axis=alt.Axis(tickCount=3, labelExpr="datum.value % 1 ? '' : format(datum.value, 'd')")),
        color=alt.Color("family:N", sort=order_fams, scale=alt.Scale(domain=order_fams, range=FAM_RANGE[:len(order_fams) - 1] + [MUTED]),
                        legend=alt.Legend(title=f"{noun} family", orient="top", direction="horizontal", columns=9)),
        tooltip=["item:N", alt.Tooltip("key:N", title=noun), "family:N",
                 alt.Tooltip("comments:Q", title="comments using it"), alt.Tooltip("pct:Q", format=".0f", title="% of comments")],
    ).properties(width=alt.Step(7.5), height=70).facet(
        facet=alt.Facet("item:N", sort=list(dict.fromkeys(df.item)), title=None,
                        header=alt.Header(labelFontSize=10.5, labelFontWeight="bold", labelAnchor="start", labelColor=INK)),
        columns=4, spacing={"row": 14, "column": 22},
    ).resolve_scale(y="independent").resolve_axis(x="independent").properties(
        title=alt.TitleParams(f"{noun.capitalize()} distribution per item: number of comments (trials) using each {noun}",
                              subtitle=f"Shared x axis = every {noun} used ≥{min_total} times overall, grouped by family. "
                                       "A comment counts once per " + noun + "; y scales are per item.",
                              anchor="start", fontSize=15))
    save(configure(chart), "op_distribution" if what == "ops" else "element_distribution")


def configure(chart):
    return (chart.configure(font="Helvetica, Arial, sans-serif", background="white")
            .configure_view(stroke=None)
            .configure_axis(labelColor=INK2, titleColor=INK2, domainColor=MUTED, tickColor=MUTED, gridColor=GRID,
                            labelFontSize=9)
            .configure_axisY(domain=False, ticks=False, grid=False)
            .configure_legend(labelFontSize=11, symbolType="square")
            .configure_title(color=INK, subtitleColor=INK2))


def save(chart, name):
    os.makedirs(OUT, exist_ok=True)
    chart.save(os.path.join(OUT, f"{name}.html"))
    chart.save(os.path.join(OUT, f"{name}.png"), scale_factor=2)
    chart.save(os.path.join(OUT, f"{name}.svg"))
    print("wrote", name)


def main():
    alt.data_transformers.disable_max_rows()
    items, meta, order = load()
    strategies_fig(items, meta, order)
    elements_fig(items, meta, order)
    heatmap_fig(items, meta, order)
    distribution_fig(items, meta, order, "ops")
    distribution_fig(items, meta, order, "elements")


if __name__ == "__main__":
    main()
