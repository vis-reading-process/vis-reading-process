"""Analyze step-trace re-coding of Nobre et al. 2024 explanations.

Inputs: trials.csv, out/text_*.jsonl (all 817, text only), out/sketch_*.jsonl (120, text+sketch),
out/reliability_coder2.jsonl (100, independent second coder). Writes results.md + figures data.
"""
import glob
import json
from collections import Counter

import pandas as pd
from sklearn.metrics import cohen_kappa_score

STAGES = ["A", "E", "C", "K"]
TYPE2STAGE = {"ATTEND": "A", "ENCODE": "A", "EXTRACT": "E", "COMPUTE": "C", "KNOW": "K"}


def load(pattern):
    rows = [json.loads(l) for f in sorted(glob.glob(pattern)) for l in open(f) if l.strip()]
    return {r["trial_id"]: r for r in rows}


def stages(r):
    # derive from steps rather than trusting the summary field
    return {TYPE2STAGE[s["type"]] for s in r.get("steps", []) if s.get("type") in TYPE2STAGE}


def seq(r, collapse=True):
    out = [s["type"] for s in r.get("steps", [])]
    if collapse:
        out = [t for i, t in enumerate(out) if i == 0 or t != out[i - 1]]
    return out


def err_family(tag):
    if not tag:
        return None
    tag = str(tag)
    return tag[0] if tag[0] in "TEDCK" else None


def first_err_family(r):
    for s in r.get("steps", []):
        f = err_family(s.get("error"))
        if f:
            # E4 lives on COMPUTE but is an "encoding" family in Nobre
            return "E" if str(s.get("error")).startswith("E4") else f
    return None


def nobre_family(codes):
    if not isinstance(codes, str) or not codes:
        return None
    for c in codes.split("; "):
        c = c.strip()
        if c[:2] in ("T1", "T2", "T3"):
            return "T"
        if c[:2] in ("E1", "E2", "E3", "E4"):
            return "E"
        if c[:2] in ("D1", "D2", "D3") or c in ("estimation mistake", "Reading Wrong Axis (X/Y)",
                                               "Read mark size instead of position", "wrong year",
                                               "wrong unit (degrees / %)", "decimal mistake"):
            return "D"
    return None


def editdist(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        prev, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (x != y))
    return d[len(b)]


def pct(x):
    return f"{100 * x:.0f}%"


def main():
    t = pd.read_csv("trials.csv").set_index("trial_id")
    text = load("out/text_*.jsonl")
    sk = load("out/sketch_*.jsonl")
    c2 = load("out/reliability_coder2.jsonl")
    L = []
    md = L.append

    missing = set(t.index) - set(text)
    md(f"# Pilot re-code results\n\nCoded trials: text {len(text)}/{len(t)} (missing {len(missing)}), "
       f"sketch {len(sk)}, reliability {len(c2)}\n")

    df = pd.DataFrame([
        dict(trial_id=k, acc=t.loc[k, "Accuracy"], chart=t.loc[k, "chart"], nobre=t.loc[k, "nobre_codes"],
             words=len(str(t.loc[k, "explanation"]).split()),
             recon=r.get("reconstructable"), n=len([s for s in r.get("steps", []) if s.get("type") != "MONITOR"]),
             order=bool(r.get("order_evidenced")), localizable=bool(r.get("error_localizable")),
             st=stages(r), seq=seq(r), ferr=first_err_family(r),
             types=[s.get("type") for s in r.get("steps", [])],
             errs=[s.get("error") for s in r.get("steps", []) if s.get("error")],
             know_roles=[(s.get("args") or {}).get("role") for s in r.get("steps", []) if s.get("type") == "KNOW"])
        for k, r in text.items() if k in t.index])
    df["acc_lbl"] = df.acc.map({0.0: "incorrect", 1.0: "correct"}).fillna("unknown")

    # 1. How much process does the existing data carry?
    md("## 1. Process information in text explanations (all trials)\n")
    md("| | all | incorrect | correct |\n|---|---|---|---|")
    groups = [df, df[df.acc == 0], df[df.acc == 1]]
    def row(name, f):
        md(f"| {name} | " + " | ".join(f(g) for g in groups) + " |")
    row("N", lambda g: str(len(g)))
    row("median words", lambda g: f"{g.words.median():.0f}")
    row("reconstructable = 0 (no process)", lambda g: pct((g.recon == 0).mean()))
    row("reconstructable = 1 (partial)", lambda g: pct((g.recon == 1).mean()))
    row("reconstructable = 2 (replayable)", lambda g: pct((g.recon == 2).mean()))
    row("≥ 2 typed steps", lambda g: pct((g.n >= 2).mean()))
    row("mean typed steps", lambda g: f"{g.n.mean():.1f}")
    row("order evidenced", lambda g: pct(g.order.mean()))
    for s, nm in zip(STAGES, ["Attend/Encode", "Extract", "Compute", "Know"]):
        row(f"stage {s} ({nm}) present", lambda g, s=s: pct(g.st.map(lambda x: s in x).mean()))
    row("all 4 stages present", lambda g: pct(g.st.map(lambda x: len(x) == 4).mean()))
    row("≥ 3 stages present", lambda g: pct(g.st.map(lambda x: len(x) >= 3).mean()))
    inc = df[df.acc == 0]
    md(f"\nIncorrect trials where the error step is localizable: **{pct(inc.localizable.mean())}**\n")

    md("### Stage combinations\n")
    combo = df.st.map(lambda x: "".join(s for s in STAGES if s in x) or "∅").value_counts()
    md("| stages | n | % |\n|---|---|---|")
    for k, v in combo.head(12).items():
        md(f"| {k} | {v} | {pct(v / len(df))} |")

    md("\n### Most common step sequences (consecutive repeats collapsed)\n")
    sq = df.seq.map(lambda x: " → ".join(x) or "∅").value_counts()
    md("| sequence | n |\n|---|---|")
    for k, v in sq.head(15).items():
        md(f"| {k} | {v} |")
    loops = df.seq.map(lambda x: len(x) != len(set(x))).mean()
    md(f"\nTraces containing a revisit/loop of a step type (e.g. ATTEND → EXTRACT → ATTEND): {pct(loops)}\n")

    md("### Step-type totals\n")
    tc = Counter(x for ts in df.types for x in ts)
    md(", ".join(f"{k} {v}" for k, v in tc.most_common()))
    kr = Counter(x for ks in df.know_roles for x in ks)
    md(f"\n\nKNOW roles: {dict(kr)}\n")
    ec = Counter(str(x).split("_")[0] if str(x)[0] != "C" else str(x) for es in df.errs for x in es)
    md(f"Step-level error tags: {dict(ec.most_common())}\n")

    md("### By chart (reconstructable = 2 rate)\n")
    bc = df.groupby("chart").agg(n=("recon", "size"), replay=("recon", lambda x: (x == 2).mean()),
                                 none=("recon", lambda x: (x == 0).mean()))
    md("| chart | n | replayable | no process |\n|---|---|---|---|")
    for c, r in bc.sort_values("n", ascending=False).iterrows():
        md(f"| {c} | {r.n} | {pct(r.replay)} | {pct(r.none)} |")

    # 2. Agreement with Nobre's trial-level barrier family
    md("\n## 2. Step-level first error vs. Nobre trial-level barrier family (incorrect trials)\n")
    inc = inc.assign(nf=inc.nobre.map(nobre_family))
    both = inc.dropna(subset=["nf"])
    md(f"Incorrect trials with a Nobre T/E/D code: {len(both)}; of these our trace localizes an error in "
       f"{pct(both.ferr.notna().mean())}.")
    b2 = both.dropna(subset=["ferr"])
    if len(b2):
        md(f" Family agreement (T/E/D, first error): **{pct((b2.ferr == b2.nf).mean())}** (n={len(b2)}); "
           f"κ = {cohen_kappa_score(b2.nf, b2.ferr):.2f}\n")
        ct = pd.crosstab(b2.nf, b2.ferr, rownames=["Nobre"], colnames=["trace first error"])
        md("```\n" + ct.to_string() + "\n```\n")

    # 3. Does the sketch add information?
    md("\n## 3. Text-only vs. text + sketch (same 120 trials)\n")
    ks = [k for k in sk if k in text]
    if ks:
        cmp = pd.DataFrame([dict(acc=t.loc[k, "Accuracy"],
                                 r_t=text[k].get("reconstructable"), r_s=sk[k].get("reconstructable"),
                                 st_t=stages(text[k]), st_s=stages(sk[k]),
                                 loc_t=bool(text[k].get("error_localizable")), loc_s=bool(sk[k].get("error_localizable")),
                                 adds=sk[k].get("sketch_adds") or []) for k in ks])
        md("| | text only | text + sketch |\n|---|---|---|")
        md(f"| replayable (=2) | {pct((cmp.r_t == 2).mean())} | {pct((cmp.r_s == 2).mean())} |")
        md(f"| no process (=0) | {pct((cmp.r_t == 0).mean())} | {pct((cmp.r_s == 0).mean())} |")
        for s in STAGES:
            md(f"| stage {s} present | {pct(cmp.st_t.map(lambda x: s in x).mean())} | {pct(cmp.st_s.map(lambda x: s in x).mean())} |")
        ci = cmp[cmp.acc == 0]
        md(f"| error localizable (incorrect, n={len(ci)}) | {pct(ci.loc_t.mean())} | {pct(ci.loc_s.mean())} |")
        md(f"\nReconstructability improved in {pct((cmp.r_s > cmp.r_t).mean())}, "
           f"unchanged {pct((cmp.r_s == cmp.r_t).mean())}, lower {pct((cmp.r_s < cmp.r_t).mean())}.\n")
        md(f"sketch_adds: {dict(Counter(a for x in cmp.adds for a in x).most_common())}\n")

    # 4. Reliability
    md("\n## 4. Inter-coder reliability (100 trials, text only)\n")
    kr_ = [k for k in c2 if k in text]
    if kr_:
        a, b = [text[k] for k in kr_], [c2[k] for k in kr_]
        md(f"n = {len(kr_)}\n\n| measure | value |\n|---|---|")
        md(f"| κ reconstructable (0/1/2, weighted) | {cohen_kappa_score([x.get('reconstructable') for x in a], [x.get('reconstructable') for x in b], weights='linear'):.2f} |")
        for s in STAGES:
            ya, yb = [s in stages(x) for x in a], [s in stages(x) for x in b]
            md(f"| κ stage {s} present | {cohen_kappa_score(ya, yb):.2f} (agree {pct(sum(p == q for p, q in zip(ya, yb)) / len(ya))}) |")
        md(f"| κ order evidenced | {cohen_kappa_score([bool(x.get('order_evidenced')) for x in a], [bool(x.get('order_evidenced')) for x in b]):.2f} |")
        fa = [first_err_family(x) or "none" for x in a]
        fb = [first_err_family(x) or "none" for x in b]
        md(f"| κ first-error family (T/E/D/C/K/none) | {cohen_kappa_score(fa, fb):.2f} |")
        ned = [editdist(seq(x), seq(y)) / max(1, len(seq(x)), len(seq(y))) for x, y in zip(a, b)]
        md(f"| mean normalized edit distance of step sequences | {sum(ned) / len(ned):.2f} |")
        md(f"| identical collapsed sequences | {pct(sum(d == 0 for d in ned) / len(ned))} |")

    open("results.md", "w").write("\n".join(L) + "\n")
    df.to_pickle("coded_text.pkl")
    print("\n".join(L))


if __name__ == "__main__":
    main()
