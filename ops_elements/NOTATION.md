# Symbolic notation for mental operations & vis elements

Goal: for each item (question × chart), write down the DIFFERENT operations people say they did (in the explanation text) or
show they did (in the sketch), as compact symbolic expressions. Capture variety — distinct strategies, including wrong ones.
Code only what the evidence shows. Do not invent steps.

## Element references (operands)
Write vis elements as `kind[detail]`. Use these kinds (add new ones if needed, and list them in `new_symbols`):
- `title`, `subtitle`, `question` (the question text itself)
- `xaxis`, `yaxis` (the axis as a whole), `xtick[2010]`, `ytick[25]` (specific tick/label), `xtitle`, `ytitle` (axis title/unit)
- `grid[y=25]` (gridline), `legend`, `legend[Soda]`, `color[green]`, `colorscale` (choropleth/heatmap ramp)
- marks: `bar[Oslo]`, `seg[Copenhagen,Sandwich]` (stacked segment), `band[Isla]` (stacked-area band), `area`, `line`,
  `pt[161cm]` / `pt[outlier]`, `bubble[Tokyo]`, `slice[Samsung]`, `tile[Amazon]`, `bin[20-40]`, `region[IN]`, `cluster[...]`
- mark parts: `top(m)`, `bottom(m)`, `edge(m)`, `peak(m)`, `center(m)`, `size(m)`, `height(m)`, `width(m)`, `angle(m)`
- `label[...]` (a text label printed on a mark), `annot[...]` (any other text or annotation printed on the chart)
- sets: `{bar[*]}` (all bars), `{pt: x∈[170,180]}`, `{xtick 2009..2014}`
- `chart` (gestalt / the whole chart), `trendline` (if they imagine one)

## Operations
Perceptual/locating:
- `LOOK(e)` — attended / looked at an element
- `FIND(e | key)` — locate an element by a key, e.g. `FIND(seg | legend[Sandwich]→color[blue], xtick[Copenhagen])`
- `MAP(e → meaning)` — an encoding belief, e.g. `MAP(color[green] → Soda)`, `MAP(size(bubble) → ridership)`
- `PROJ(e → axis)` — project/trace from a mark to an axis (a horizontal/vertical line in a sketch is strong evidence)
- `READ(e, channel) = v` — read a value; channel ∈ {y, x, len, h, area, size, angle, color, label}. Use `≈v` for estimates, `v?` when not stated
- `INTERP(v | ticks a,b)` — interpolate between ticks
- `SCAN({set})` — sweep over many marks
- `GIST(chart) → claim` — holistic / "just saw it" judgement with no decomposition
Computational:
- `CMP(a ? b)` with `?` ∈ {>, <, =, ≈}; also `CMPvis(size(a) > size(b))` when the comparison is purely visual
- `ARGMAX/ARGMIN(set, channel)`, `MAX/MIN`
- `DIFF(a,b)`, `SUM(...)`, `RATIO(a,b)`, `PCT(part,whole)`, `AVG(...)`, `RANGE(min,max)`, `COUNT(set | cond)`
- `SEG(top − bottom)` — a stacked-segment length obtained by subtracting
- `TREND(series, interval) ∈ {↑, ↓, →, ~}`, `SLOPE`, `CORR(x,y) ∈ {+, −, 0}`
- `GROUP(set) → cluster`, `OUTLIER(set) → e`
Knowledge/meta:
- `KNOW(claim)` — prior/world knowledge or term definition
- `DOUBT(x)`, `CONFUSED(x)`, `CHECK(x)`, `GUESS`, `FIX(x→y)` (self-correction, e.g. noticed while drawing)
- `?wrong` suffix on any step that is evidently mistaken, e.g. `READ(top(seg[Copenhagen,Sandwich]), y)=24 ?wrong:read-cumulative-top-not-share`

Chain steps with `→` in the order the participant gives (or the logical order if no order is given).
A strategy is one chain, e.g.
  `FIND(seg[Copenhagen,Sandwich]) → PROJ(top → yaxis) → READ(y)=24 → ANSWER(24)` ?wrong: treated cumulative height as %
