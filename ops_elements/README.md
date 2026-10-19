# Mental operations & vis elements per item (Nobre et al. 2024 trials)

Every trial (817 trials, 49 question × chart items) was coded from its explanation **and** its sketch. Each trial has
- an ordered **operation chain** in symbolic notation (`NOTATION.md`),
- the vis **elements mentioned in the text**,
- the vis **elements marked in the sketch**.

Each item then has its distinct strategies listed with counts.

| file | contents |
|---|---|
| `NOTATION.md` | operation and element vocabulary |
| `items.md` | **per item**: reference chain, every distinct strategy (n, ✓/✗, quote), operation counts, element counts (text / sketch) |
| `summary.md` | **across items**: operation and element families by task type and by chart type, text-vs-sketch split, task × chart top-3 tables |
| `coded/*.json` | raw per-trial codes (`chain`, `ops`, `elements_text`, `elements_sketch`, `sketch_gesture`, `source`) |
| `items_meta.json` | the task-type and chart-type label for each item (my VLAT-style assignment) |
| `aggregate.py` | regenerates `items.md` and `summary.md` from `coded/` |

**How it was coded.** 7 Claude subagents (one per chart group) read every composite image (chart + sketch + text) and coded against a shared notation. There was one coder per trial and no reliability pass, so treat counts as approximate. The `ops` lists vary somewhat across coders, e.g. LOOK vs FIND, and whether ANSWER is listed. 87% of chains rest on text + sketch, 11% on the sketch alone, and 2% on text alone.

---

## Cross-item patterns

### 1. One backbone, with task-specific operators added on top

Almost every chain is built from **locate → extract → operate**:

```
FIND(mark | key: xtick / legend / label) → PROJ(mark → axis) → READ(channel) = v  → task operator
```

- `PROJ` appears in 41% of all trials. It is mostly visible in the sketch: L-shaped lines from a tick to the mark and then to the axis.
- In retrieval items, 47% of trials contain the full FIND…PROJ…READ chain and 72% contain a PROJ.

The task determines the operator added at the end. It also determines where the chain usually breaks.

| task | typical chain | where it breaks |
|---|---|---|
| retrieve value | `FIND(xtick, legend) → PROJ → READ(y)` | wrong **channel**: top-edge position instead of segment/band length (SA, SB, SB100), angle in degrees read as % (pie), wrong colour-bin label (choropleth). Wrong **key**: wrong year or month on sparsely labelled date axes (AC) |
| make comparison | `FIND(a) → FIND(b) → CMPvis(a ? b)`, often **without reading values**. Histograms: `PROJ(top ↔ top)` reference line | stacked charts: `CMP(top(a) > top(b))` instead of lengths. The visual-only comparison works on bubbles, treemap and histogram |
| find extremum | `SCAN(set) → ARGMAX(set, channel)` | ARGMAX on the wrong channel: `top-y` vs `len` (SB), `size` vs `x` (bubble), `y` vs `x` (scatter "tallest"). Share vs count (SB100). `MISSING(scale)` (treemap) |
| determine range | `ARGMIN/ARGMAX → PROJ → READ ×2 → RANGE` | 30/68 read the **axis extent** (`READ(ytick[min], ytick[max])`) as the data range. 10/68 used the **endpoints** of the interval instead of its extrema |
| characterize trend | `TRACE(edge, interval) → TREND ∈ {↑,↓,→}` | traced the cumulative top edge (SA). Did not restrict to the asked interval (LC, AC2) |
| correlation | scatter: `SCAN → FIT(trendline) → SLOPE → CORR`. Bubble: **counterexample** `FIND(high-x small bubble) → CMP(size vs x) → CORR≠+` | confusion over the wording "negative linear". Prior knowledge (`KNOW`) used instead of the data |
| clusters | **crosshair**: `FIND(xtick) & FIND(ytick) → PROJ → LOOK(region) → COUNT(pts)=0` | few errors |
| derived value | `READ ×k → SUM / DIFF / AVG` | bin selection (HC: including 10–20). Arithmetic and entry slips (LC). Treating the mean as "a bubble at (300, 200)" (BuC) |

### 2. Chart type decides which *element* is pivotal

- **Stacked charts (SA, SB, SB100; 360 trials).** The pivotal element is a mark *part*: `top(band|seg)` vs `height/len(band|seg)`.
  - 191 trials (53%) contain an error where a top-edge or cumulative position stood in for a length.
  - This one confusion explains most wrong answers on 13 items.
  - Correct answers come from `SEG(top − bottom)`, from brackets or double arrows across a band, or from direct `CMPvis(len)`.
- **Bubble.**
  - Size vs position: `MAP(size → ridership)` via the legend circles (3.0/3.5) vs `x = stations`.
  - Range questions pull people to the axis end ticks.
- **Area / line.** `xtick` is pivotal. Only Jan/Apr/Jul/Oct are labelled and the year appears under Jan, which causes off-by-one month and wrong-year errors.
- **Histogram.** `bin` edges vs labels. Variant 2's range labels ("20–30") moved errors from bin selection to reading and summing.
- **Scatter.** Points, both axes, and an **imagined trendline**: 20% of scatter trials drew one.
- **Treemap.** No axes are mentioned at all. Only tiles, labels and the absence of a scale (`MISSING`).
- **Pie.** Angle → %. **Choropleth.** Region → colour → swatch → bin label.

### 3. Text and sketch surface different elements (`summary.md`, "text vs sketch")

- **Axes/ticks and marks** show up far more in sketches than in text. For example, on stacked area charts axes/ticks appear in 31% of texts vs 58% of sketches, and marks in 34% vs 99%. People draw projection lines but rarely write "I read the y-axis".
- **Legend/colour** is the reverse: it is mostly in the text ("the green one", "the colour for Isla"), because people use the legend without drawing on it.
- **Gridlines, titles and annotations** are almost never mentioned. The exceptions are SB100, where the "%" in the axis title cued the correct answer, and the treemap, which has labels.
- **"Whole chart" / GIST** is text-only. It never shows up as a sketch target.
- **Prior knowledge (`KNOW`)** is rare: 29/817 trials. It concentrates on SB100Q3, where people knew the segments are shares and not counts, and on BuCQ4 (beliefs about metros).

### 4. Things to check before using the accuracy column

The coders flagged likely **scoring errors** in the source data:
- ACQ4: all 14 trials answered "Constant", which is the shown key, but are scored 0.
- SAQ3: "2014" matches the key but is scored 0.
- SAQ4: "Rising" is scored 1 even though the key is "Falling".
- BuCQ2 and SPQ3: correct min/max answers are scored 0, possibly because of the field order.
- BCQ3: one 12/99 answer is scored 0.

The ✓/✗ counts in `items.md` use the original scores. `coded/g2_SA.json` adds `correct_by_key` for SAQ3–4.
