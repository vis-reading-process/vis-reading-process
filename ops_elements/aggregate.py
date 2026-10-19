"""Aggregate per-trial symbolic codes (coded/*.json) into per-item and cross-item tables.

Run from repo root:  python3 ops_elements/aggregate.py
Writes ops_elements/items.md (per item) and ops_elements/summary.md (by task / chart type).
"""
import collections
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = {"top", "bottom", "edge", "peak", "valley", "center", "mid", "size", "height", "width", "angle", "len",
         "outline", "area", "shape"}
MARKS = {"seg", "band", "bubble", "pt", "bin", "tile", "bar", "slice", "region", "line", "area", "cluster", "group", "mark"}
EL_FAMILY = {"axis/ticks": {"xaxis", "yaxis", "xtick", "ytick", "xtitle", "ytitle"}, "data marks": MARKS,
             "legend/color": {"legend", "color", "colorscale"}, "gridline": {"grid"},
             "text/annot": {"title", "subtitle", "label", "annot"}, "whole chart": {"chart"},
             "imagined guide": {"trendline", "template", "envelope", "trend", "slope"}, "question": {"question"}}
OP_FAMILY = {"locate": {"LOOK", "FIND", "SCAN"}, "encode": {"MAP"},
             "extract": {"PROJ", "READ", "INTERP", "TRACE", "SEG"},
             "compare": {"CMP", "CMPvis", "ARGMAX", "ARGMIN", "MAX", "MIN"},
             "arithmetic": {"DIFF", "SUM", "RATIO", "PCT", "AVG", "RANGE", "COUNT"},
             "pattern": {"TREND", "SLOPE", "CORR", "FIT", "GROUP", "OUTLIER", "GIST"},
             "knowledge": {"KNOW"}, "monitor": {"DOUBT", "CONFUSED", "CHECK", "FIX", "GUESS", "MISSING"},
             "sketch-only": {"LABEL", "OVERLAY", "SPLIT", "DRAW"}}
OP_ALIAS = {"MAX/MIN": "MAX"}


def ops_of(t):
    return [OP_ALIAS.get(o, o) for o in t["ops"] if o != "ANSWER"]


def family(name, table_):
    for f, members in table_.items():
        if name in members:
            return f
    return "other"


def load():
    items = {}
    for f in sorted(glob.glob(os.path.join(HERE, "coded", "*.json"))):
        items.update(json.load(open(f)))
    return items


def kind(e):
    """'top(seg[Copenhagen,Sandwich])' -> 'seg'; 'legend[Soda]' -> 'legend'; 'yaxis' -> 'yaxis'."""
    e = e.strip()
    m = re.match(r"^(\w+)\((.*)\)$", e)
    if m and m.group(1) in PARTS:
        return kind(m.group(2))
    m = re.match(r"^\{?\s*(\w+)", e)
    k = m.group(1).lower() if m else e
    return "mark" if k in PARTS and k not in MARKS else k


def part(e):
    m = re.match(r"^(\w+)\(", e.strip())
    return m.group(1) if m and m.group(1) in PARTS else None


def pct(n, d):
    return f"{100 * n / d:.0f}%" if d else "–"


def item_stats(it):
    tr = it["trials"]
    ops = collections.Counter(o for t in tr for o in set(ops_of(t)))
    et = collections.Counter(k for t in tr for k in {kind(e) for e in t["elements_text"]})
    es = collections.Counter(k for t in tr for k in {kind(e) for e in t["elements_sketch"]})
    parts = collections.Counter(p for t in tr for p in {part(e) for e in t["elements_text"] + t["elements_sketch"]} if p)
    detail = collections.Counter(e for t in tr for e in set(t["elements_text"]) | set(t["elements_sketch"]))
    return dict(n=len(tr), ops=ops, et=et, es=es, parts=parts, detail=detail,
                empty=sum(1 for t in tr if t["chain"].strip() in ("∅", "")),
                correct=sum(1 for t in tr if t["accuracy"] == 1))


def table(rows, head):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def write_items(items, meta):
    order = sorted(items, key=lambda q: (meta[q]["chart"], q))
    L = ["# Operations & elements per item\n",
         "Notation: see `NOTATION.md`. Counts are trials. *text* = mentioned in the explanation, *sketch* = marked in the drawing.\n"]
    for q in order:
        it, s = items[q], item_stats(items[q])
        L += [f"## {q} · {meta[q]['chart_type']} · {meta[q]['task']}",
              f"> {it['question']}\n",
              f"n = {s['n']} (correct {s['correct']}), no process info: {s['empty']}\n",
              f"**Reference:** `{esc(it.get('reference_chain', ''))}`\n",
              f"{it.get('notes', '')}\n",
              "**Strategies people used**\n"]
        sts = sorted(it["strategies"], key=lambda st: -st["n"])  # same order/S# as figures/strategies
        L.append(table([[f"S{i}", f"`{esc(st['chain'])}`", st["n"], st.get("n_correct", ""), st.get("n_incorrect", ""),
                         f"“{esc(st.get('quote', ''))}”"] for i, st in enumerate(sts, 1)],
                       ["#", "chain", "n", "✓", "✗", "example"]))
        L.append("\n**Operations** (trials using it): " +
                 ", ".join(f"`{o}` {c}" for o, c in s["ops"].most_common()) + "\n")
        kinds = sorted(set(s["et"]) | set(s["es"]), key=lambda k: -(s["et"][k] + s["es"][k]))
        L.append("**Elements** (kind: text / sketch): " +
                 ", ".join(f"`{k}` {s['et'][k]}/{s['es'][k]}" for k in kinds) + "\n")
        L.append("**Specific elements:** " + ", ".join(f"`{esc(e)}` {c}" for e, c in s["detail"].most_common(12)) + "\n")
        if it.get("new_symbols"):
            L.append("**New symbols:** " + "; ".join(f"`{k}`: {esc(v)}" for k, v in it["new_symbols"].items()) + "\n")
    open(os.path.join(HERE, "items.md"), "w").write("\n".join(L))


def group_table(items, meta, key, title):
    groups = collections.defaultdict(list)
    for q, it in items.items():
        groups[key(q)].append(it)
    L = [f"## {title}\n"]
    for g in sorted(groups, key=lambda g: -sum(len(i["trials"]) for i in groups[g])):
        its = groups[g]
        tr = [t for i in its for t in i["trials"]]
        n = len(tr)
        ops = collections.Counter(o for t in tr for o in set(ops_of(t)))
        et = collections.Counter(k for t in tr for k in {kind(e) for e in t["elements_text"]})
        es = collections.Counter(k for t in tr for k in {kind(e) for e in t["elements_sketch"]})
        anyel = collections.Counter(k for t in tr for k in {kind(e) for e in t["elements_text"] + t["elements_sketch"]})
        seqs = collections.Counter(collapse(ops_of(t)) for t in tr)
        L += [f"### {g}  (n = {n} trials, items: {', '.join(sorted(i['qid'] for i in its))})\n",
              "Top operations: " + ", ".join(f"`{o}` {pct(c, n)}" for o, c in ops.most_common(10)) + "  ",
              "Top elements (any / text / sketch): " +
              ", ".join(f"`{k}` {pct(c, n)}/{pct(et[k], n)}/{pct(es[k], n)}" for k, c in anyel.most_common(10)) + "  ",
              "Common op sequences: " + ", ".join(f"`{s}` {c}" for s, c in seqs.most_common(6)) + "\n"]
    return "\n".join(L)


def collapse(ops):
    out = []
    for o in ops:
        if not out or out[-1] != o:
            out.append(o)
    return " → ".join(out) or "∅"


def matrix(items, meta, what):
    """task × chart cell: top-3 ops or elements."""
    cells = collections.defaultdict(list)
    for q, it in items.items():
        cells[(meta[q]["task"], meta[q]["chart_type"])] += it["trials"]
    tasks = sorted({k[0] for k in cells})
    charts = sorted({k[1] for k in cells})
    rows = []
    for tk in tasks:
        row = [tk]
        for ch in charts:
            tr = cells.get((tk, ch), [])
            if not tr:
                row.append("")
                continue
            if what == "ops":
                c = collections.Counter(o for t in tr for o in set(ops_of(t)))
            else:
                c = collections.Counter(k for t in tr for k in {kind(e) for e in t["elements_text"] + t["elements_sketch"]})
            row.append(f"n={len(tr)}: " + ", ".join(f"{o} {pct(v, len(tr))}" for o, v in c.most_common(3)))
        rows.append(row)
    return table(rows, ["task \\ chart"] + charts)


def family_matrix(items, meta, groupkey, what):
    cells = collections.defaultdict(list)
    for q, it in items.items():
        cells[groupkey(q)] += it["trials"]
    fams = list(OP_FAMILY if what == "ops" else EL_FAMILY)
    rows = []
    for g in sorted(cells, key=lambda g: -len(cells[g])):
        tr = cells[g]
        if what == "ops":
            per = [{family(o, OP_FAMILY) for o in ops_of(t)} for t in tr]
        else:
            per = [{family(kind(e), EL_FAMILY) for e in t["elements_text"] + t["elements_sketch"]} for t in tr]
        rows.append([g, len(tr)] + [pct(sum(f in p for p in per), len(tr)) for f in fams])
    return table(rows, ["group", "n"] + fams)


def text_vs_sketch(items, meta):
    """Per chart type: share of trials where each element family appears in text vs sketch."""
    cells = collections.defaultdict(list)
    for q, it in items.items():
        cells[meta[q]["chart_type"].split("(")[0]] += it["trials"]
    fams = [f for f in EL_FAMILY if f not in ("imagined guide", "question")]
    rows = []
    for g in sorted(cells, key=lambda g: -len(cells[g])):
        tr = cells[g]
        row = [g, len(tr)]
        for f in fams:
            nt = sum(any(family(kind(e), EL_FAMILY) == f for e in t["elements_text"]) for t in tr)
            ns = sum(any(family(kind(e), EL_FAMILY) == f for e in t["elements_sketch"]) for t in tr)
            row.append(f"{pct(nt, len(tr))} / {pct(ns, len(tr))}")
        rows.append(row)
    return table(rows, ["chart", "n"] + [f + " (text / sketch)" for f in fams])


def main():
    meta = json.load(open(os.path.join(HERE, "items_meta.json")))
    items = load()
    write_items(items, meta)
    L = ["# Common operations & elements across task and chart type\n",
         f"{sum(len(i['trials']) for i in items.values())} trials, {len(items)} items. "
         "Percentages = share of trials in the group whose code uses the operation/element (text or sketch).\n",
         "## Operation families by task\n", family_matrix(items, meta, lambda q: meta[q]["task"], "ops"),
         "\n## Operation families by chart\n",
         family_matrix(items, meta, lambda q: meta[q]["chart_type"].split("(")[0], "ops"),
         "\n## Element families by task\n", family_matrix(items, meta, lambda q: meta[q]["task"], "elements"),
         "\n## Element families by chart\n",
         family_matrix(items, meta, lambda q: meta[q]["chart_type"].split("(")[0], "elements"),
         "\n## Where elements show up: text vs sketch\n", text_vs_sketch(items, meta),
         "\n## Task × chart: top operations\n", matrix(items, meta, "ops"),
         "\n## Task × chart: top elements\n", matrix(items, meta, "elements"), "",
         group_table(items, meta, lambda q: meta[q]["task"], "By task type"),
         group_table(items, meta, lambda q: meta[q]["chart_type"].split("(")[0], "By chart type")]
    open(os.path.join(HERE, "summary.md"), "w").write("\n".join(L))
    print("wrote items.md, summary.md")


if __name__ == "__main__":
    main()
