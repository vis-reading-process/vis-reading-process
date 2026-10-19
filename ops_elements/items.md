# Operations & elements per item

Notation: see `NOTATION.md`. Counts are trials. *text* = mentioned in the explanation, *sketch* = marked in the drawing.

## ACQ1 · area · retrieve_value
> What was the price of a pound of coffee beans in June 2019?

n = 6 (correct 0), no process info: 0

**Reference:** `FIND(xtick[June 2019] \| xtick[April 2019], xtick[July 2019]) → PROJ(xtick[June 2019] → top(area)) → PROJ(top(area) → yaxis) → INTERP(v \| ticks 0.70,0.75) → READ(top(area), y)≈0.71 → ANSWER(0.71)`

All six trials are incorrect, and every sketch shows the projection idea (vertical up from the x-axis, horizontal over to the y-axis) carried out at the wrong place or reported in the wrong format. The main pitfall is the x-axis: June has no label (only Jan/Apr/Jul/Oct ticks), and the chart covers two years, so three people projected from June 2018 (≈0.86–0.89) and others landed on July 2019 or Jan 2019. Two people found the right spot but typed the value as a percentage-like integer (72, 74), dropping the '0.' of the $/lb scale.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(xtick[June 2018]) ?wrong:wrong-year → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → READ(top(area), y)≈0.88 → ANSWER(v)` | 3 | 0 | 3 | “the peak of the price was clear” |
| `FIND(xtick[June 2019]) → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → READ(top(area), y)≈0.72 → ANSWER(72) ?wrong:dropped-decimal-scale` | 1 | 0 | 1 | “found june on bottom axis and drew a line across to price axis” |
| `FIND(xtick[June 2019]) → FIND(top(area)[July 2019]) ?wrong:wrong-month → READ(top(area), y)≈0.74 → ANSWER(74) ?wrong:dropped-decimal-scale` | 1 | 0 | 1 | “Find june and point the price” |
| `FIND(xtick[Jan 2019]) ?wrong:wrong-month → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → CONFUSED(no ticks between 0.75 and 0.80) → INTERP(v \| ticks 0.75,0.80) → READ(y)≈0.76 → ANSWER(0.76)` | 1 | 0 | 1 | “it was a little confusing since the were no values between 0.75 and 0.80” |

**Operations** (trials using it): `READ` 6, `FIND` 6, `PROJ` 4, `INTERP` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `xtick` 2/4, `mark` 0/6, `yaxis` 2/3, `xaxis` 1/0, `chart` 1/0, `ytick` 1/0, `area` 1/0

**Specific elements:** `yaxis` 4, `xtick[June]` 2, `top(area)[June 2018]` 2, `xtick[June 2018]` 2, `top(area)[July 2019]` 1, `top(area)[June-July 2018]` 1, `chart` 1, `ytick[0.80]` 1, `ytick[0.75]` 1, `top(area)[Jan 2019]` 1, `xtick[Jan 2019]` 1, `top(area)[June 2019]` 1

## ACQ2 · area · find_extremum
> When was the price of a pound of coffee beans at a minimum?

n = 8 (correct 0), no process info: 0

**Reference:** `SCAN({top(area) Jan 2018..Jan 2020}) → ARGMIN({top(area)}, y) = pt[Nov 2019] → PROJ(pt → xaxis) → INTERP(month \| xtick[October 2019], xtick[January 2020]) → READ(x)=Nov 2019 → ANSWER(Nov 2019)`

All eight trials are incorrect, but half of them did find the right dip: they dropped a vertical line from the Nov 2019 trough and then named the wrong month (Oct 2019, or Nov 2018). The failure is at the very end, mapping a position on the x-axis to a month: there are minor ticks but only every third month is labelled, so the dip just right of the 'October' label gets read as October. Other errors were choosing the wrong mark altogether: the last point (Jan 2020, twice) or the maximum (Mar 2018). The horizontal line people drew to the y-axis shows they were checking the minimum's value even though the question asks for a time.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `ARGMIN({top(area)}, y) = pt[Nov 2019] → PROJ(pt → xaxis) → PROJ(pt → yaxis) → READ(x)=Oct 2019 ?wrong:off-by-one-month-unlabeled-ticks → ANSWER(Oct 2019)` | 4 | 0 | 4 | “When I drew the lines I noticed that I answered the wrong month. So I realized that I was confused by the way the months were organized.” |
| `ARGMIN({top(area)}, y) = pt[Jan 2020] ?wrong:picked-last-point-not-min → PROJ(pt → xaxis) → ANSWER(Jan 2020)` | 2 | 0 | 2 | “The lowest recorded price was in January 2020” |
| `SCAN({top(area)}) → ARGMIN("biggest dip") = pt[Nov 2019] → PROJ(pt → xaxis) → READ(x)=Nov 2018 ?wrong:wrong-year → ANSWER(Nov 2018)` | 1 | 0 | 1 | “I just looked for the biggest dip.” |
| `FIND(peak(area)[Mar 2018]) ?wrong:picked-maximum-not-minimum → ANSWER(Mar 2018)` | 1 | 0 | 1 | “It was easy to analyze the chart” |

**Operations** (trials using it): `ARGMIN` 7, `PROJ` 6, `READ` 5, `CONFUSED` 2, `SCAN` 1, `FIND` 1, `FIX` 1, `DOUBT` 1

**Elements** (kind: text / sketch): `pt` 1/7, `xaxis` 0/5, `yaxis` 0/5, `xtick` 3/1, `mark` 1/1, `chart` 1/0

**Specific elements:** `xaxis` 5, `pt[Nov 2019 trough]` 5, `yaxis` 5, `xtick[*]` 2, `xtick[January 2020]` 2, `pt[Jan 2020]` 2, `xtick[November]` 1, `peak(area)[dip]` 1, `chart` 1, `peak(area)[Mar 2018]` 1, `pt[min]` 1

## ACQ3 · area · determine_range
> What was the range of the price of a pound of coffee beans between January 2018 and January 2020?

n = 13 (correct 0), no process info: 0

**Reference:** `SCAN({top(area) Jan 2018..Jan 2020}) → MAX({top(area)}, y)=pt[Mar 2018] → PROJ(pt → yaxis) → READ(y)≈0.89 → MIN({top(area)}, y)=pt[Nov 2019] → PROJ(pt → yaxis) → READ(y)≈0.69 → RANGE(0.69, 0.89) → ANSWER(0.69–0.89)`

All 13 trials are incorrect, and they fail in three different ways. (1) Endpoint substitution (5 trials): reading the price in Jan 2018 and Jan 2020 (0.89/0.73) instead of the max and min, i.e. treating the range of time as the range of price. (2) Axis-range substitution (3 trials): circling or tracing the y-axis bounds 0.90/0.50, so the y-axis frame stands in for the data. (3) Correct max/min search with an error at the output: a digit transposition (0.98, 0.99), dropping the decimal (88/68), or typing a value that doesn't match the sketch (0.78). The early-2018 plateau also made the maximum ambiguous ('more constant with the surrounding prices').

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(top(area)[Jan 2018]) → READ(y)≈0.89 → FIND(top(area)[Jan 2020]) → READ(y)≈0.73 → RANGE(first, last) ?wrong:endpoints-not-extrema → ANSWER(0.89/0.73)` | 5 | 0 | 5 | “The range I just looked were the graph started and were it ended” |
| `MAX({top(area)}, y) → PROJ(→ yaxis) → READ(y)≈0.89 → MIN({top(area)}, y)=pt[Nov 2019] → PROJ(→ yaxis) → READ(y)≈0.69 → ANSWER(v) ?wrong:entry-error(transposed digits / dropped decimal / mismatched value)` | 4 | 0 | 4 | “I looked at the highest point of the graph and the lowest point of the graph.” |
| `LOOK(yaxis) → READ(ytick[0.90])=0.90 → READ(ytick[0.50])=0.50 → RANGE(axis bounds) ?wrong:axis-range-not-data-range → ANSWER(0.90/0.50)` | 2 | 0 | 2 | “A range is a measurement between two numbers” |
| `MAX({top(area)}, y) → READ(y)≈0.89 → MIN({top(area)}, y) → READ(y)≈0.68 → FIX(min → ytick[0.50]) ?wrong:axis-minimum-not-data-minimum → ANSWER(0.89/0.5)` | 1 | 0 | 1 | “I put the minimum figure possible instead of the lowest figure that was actually there” |
| `FIND(top(area)[Jan-Feb 2018]) → READ(y)≈0.88 → READ(y)=0.85? ?wrong:only-early-region-inspected → ANSWER(0.88/0.85)` | 1 | 0 | 1 | “Clarity of the chart” |

**Operations** (trials using it): `READ` 13, `RANGE` 7, `FIND` 6, `MIN` 5, `PROJ` 5, `MAX` 5, `DOUBT` 2, `LOOK` 2, `KNOW` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `pt` 3/10, `yaxis` 2/5, `mark` 0/6, `xtick` 2/2, `area` 4/0, `ytick` 2/1, `xaxis` 0/1, `grid` 0/1, `chart` 1/0

**Specific elements:** `yaxis` 7, `pt[Nov 2019 trough]` 5, `pt[Jan 2020]` 5, `pt[Jan 2018]` 5, `peak(area)` 4, `ytick[0.50]` 2, `xtick[January 2020]` 2, `xtick[January 2018]` 2, `top(area)` 1, `peak(area)[Feb-Mar 2018]` 1, `pt[first]` 1, `pt[last, January]` 1

**New symbols:** `valley(m)`: mark part: a local/global trough of a line/area top (counterpart of peak(m))

## ACQ4 · area · characterize_trend
> Over the first 6 months of 2018, the price of a pound of coffee beans was roughly ____________.'

n = 14 (correct 0), no process info: 0

**Reference:** `FIND({xtick Jan..Jun 2018}) → SCAN({top(area) Jan..Jun 2018}) → RANGE(min, max)≈0.88–0.89 → TREND(area, Jan-Jun 2018)=→ → ANSWER(Constant)`

Every one of the 14 trials answered 'Constant', which is the study's answer key for this item (shown on other ACQ4 composites as 'correct answer: Constant'), yet all are coded accuracy 0. That looks like a scoring or data artifact, so none of the chains are marked ?wrong. The sketches are strikingly uniform: a line or ellipse along the flat area top over Jan–Jun 2018, usually closed off by a vertical line at about June/July to mark the end of the interval. The pivotal elements are the x-axis interval boundary (July, after which the price drops) and the flatness of top(area). Text explanations add net-change reasoning: rises cancel falls, the average, no peaks or lows, minor difference.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND({xtick Jan..Jun 2018}) → [PROJ(→ top(area))] → LOOK(top(area)[Jan-Jun 2018]) → TREND(area, interval)=→ → ANSWER(Constant)` | 4 | 0 | 4 | “I marked 6 first months of 2018 and saw that the price wasn't changing much” |
| `LOOK(top(area)[Jan-Jun 2018]) → [GIST] → TREND(area, interval)=→ → ANSWER(Constant)` | 4 | 0 | 4 | “It looks constant throughout that period” |
| `LOOK(top(area)[Jan-Jun 2018]) → SCAN(local ↑/↓) → CMP(rise ≈ fall) → TREND(area, interval)=→ → ANSWER(Constant)` | 3 | 0 | 3 | “I saw that it was rising but also decreasing at the same rate” |
| `LOOK(top(area)[Jan-Jun 2018]) → DIFF(start,end)≈small → TREND(area, interval)=→ → ANSWER(Constant)` | 1 | 0 | 1 | “there was not much difference to the prices over the 6 months the change in the price was minor” |
| `LOOK(top(area)[Jan-Jun 2018]) → TREND=→ → FIND(xtick[July 2018]) → TREND(after July)=↓ → ANSWER(Constant)` | 1 | 0 | 1 | “It looked like rather steady line until July, when it obviously starts dropping” |
| `FIND({xtick Jan..Jun 2018}) → LOOK(top(area)[Jan-Jun 2018]) → AVG(top(area)[interval]) → TREND(area, interval)=→ → ANSWER(Constant)` | 1 | 0 | 1 | “Tried to find the average within that time period” |

**Operations** (trials using it): `TREND` 14, `LOOK` 14, `FIND` 6, `CMP` 2, `PROJ` 2, `GIST` 1, `SCAN` 1, `AVG` 1, `COUNT` 1, `DOUBT` 1, `DIFF` 1

**Elements** (kind: text / sketch): `mark` 4/14, `xtick` 6/9, `chart` 4/0, `area` 2/0, `line` 1/0, `ytick` 1/0

**Specific elements:** `top(area)[Jan-Jun 2018]` 14, `{xtick Jan..Jun 2018}` 5, `xtick[June/July 2018]` 5, `chart` 4, `top(area)[rises/falls]` 2, `xtick[dates provided]` 1, `top(area)[monthly falls/rises]` 1, `xtick[July 2018]` 1, `line` 1, `xtick[July]` 1, `xtick[*]` 1, `area` 1

**New symbols:** `valley(m)`: mark part: a trough on a line/area top (counterpart of peak(m))

## AC2Q1 · area(variant 2) · retrieve_value
> What was the price of a pound of coffee beans in May 2019?

n = 6 (correct 0), no process info: 0

**Reference:** `FIND(xtick[May 2019] \| xtick[April 2019], xtick[July 2019]) → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → INTERP(v \| ticks 0.70,0.75) → READ(y)≈0.72 → ANSWER(0.72)`

All six trials draw the textbook vertical-then-horizontal projection, so the errors are in choosing the anchor or in writing the answer. Two people anchored on May 2018 rather than May 2019 (the year labels sit only under the January ticks), and one anchored near Aug 2019. Three projected from the right spot (May 2019, ~0.72), but two of them typed '73', dropping the '0.' of the $/lb scale (one said 'a bit confusing about the pound'), and one rounded up to 0.74.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(xtick[May 2019]) → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → READ(y)≈0.72-0.73 → ANSWER(v) ?wrong:format-or-rounding(73 / 0.74)` | 3 | 0 | 3 | “It was a bit confusing about the pound” |
| `FIND(xtick[May 2018]) ?wrong:wrong-year → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → READ(y)≈0.83 → ANSWER(0.83)` | 2 | 0 | 2 | “Just located may between april and july” |
| `FIND(xtick[Aug 2019]) ?wrong:wrong-month → PROJ(xtick → top(area)) → PROJ(top(area) → yaxis) → READ(y)≈0.69 → ANSWER(0.73) ?wrong:answer-mismatches-sketch` | 1 | 0 | 1 | “I started from the month” |

**Operations** (trials using it): `READ` 6, `PROJ` 6, `FIND` 6, `CONFUSED` 1

**Elements** (kind: text / sketch): `xtick` 2/6, `yaxis` 1/6, `mark` 0/6, `ytitle` 1/0, `xaxis` 1/0, `pt` 1/0, `ytick` 0/1

**Specific elements:** `yaxis` 6, `top(area)[May 2019]` 3, `xtick[May 2019]` 3, `top(area)[May 2018]` 2, `xtick[May 2018]` 2, `xtick[~Aug 2019]` 1, `xtick[month]` 1, `top(area)[Aug 2019]` 1, `ytick[0.73]` 1, `xtick[May]` 1, `xtick[April]` 1, `xtick[July]` 1

## AC2Q2 · area(variant 2) · find_extremum
> When was the price of a pound of coffee beans at a minimum?

n = 3 (correct 0), no process info: 0

**Reference:** `SCAN({top(area)}) → ARGMIN({top(area)}, y)=pt[Aug 2019] → PROJ(pt → xaxis) → INTERP(month \| xtick[July 2019], xtick[October 2019]) → READ(x)=Aug 2019 → ANSWER(Aug 2019)`

All three people found the correct trough (Aug 2019), as their sketches show, and all three went wrong converting its x-position into a month and year. That conversion is the pivotal step here, since only Jan/Apr/Jul/Oct are labelled and the year appears only under January. One person even wrote 'August' on the sketch but typed Sep 2019, then noticed the slip ('they werent labeled'); another got the month right and the year wrong (2018).

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `ARGMIN({top(area)}, y)=pt[Aug 2019] → PROJ(pt → xaxis) → READ(x)=Sep 2019 ?wrong:off-by-one-month-unlabeled-ticks → ANSWER(Sep 2019)` | 2 | 0 | 2 | “It's Aug 2019. I just didnt look at the data properly because they werent labeled.” |
| `ARGMIN({top(area)}, y)=pt[Aug 2019] → READ(x)=Aug 2018 ?wrong:wrong-year → ANSWER(Aug 2018)` | 1 | 0 | 1 | “the lowest point on the chart” |

**Operations** (trials using it): `READ` 3, `ARGMIN` 3, `PROJ` 2, `FIX` 1

**Elements** (kind: text / sketch): `pt` 1/3, `xaxis` 0/2, `xtick` 1/0, `annot` 0/1, `yaxis` 0/1, `chart` 1/0

**Specific elements:** `pt[Aug 2019 trough]` 3, `xaxis` 2, `pt[lowest]` 1, `chart` 1, `annot[August (participant-written)]` 1, `yaxis` 1, `xtick[*] (unlabeled months)` 1

## AC2Q3 · area(variant 2) · determine_range
> What was the range of the price of a pound of coffee beans between January 2018 and January 2020?

n = 7 (correct 0), no process info: 0

**Reference:** `SCAN({top(area) Jan 2018..Jan 2020}) → MAX({top(area)}, y)=peak(area)[Nov 2018] → PROJ(→ yaxis) → READ(y)≈0.89 → MIN({top(area)}, y)=pt[Aug 2019] → PROJ(→ yaxis) → READ(y)≈0.69 → RANGE(0.69, 0.89) → ANSWER(0.69–0.89)`

As on ACQ3, the dominant error is reading the two January endpoints (≈0.78/0.75) instead of the extrema (4 of 7). The question's 'between January 2018 and January 2020' wording invites this, and one person said they weren't sure whether only the two Januaries were meant. The three who did use max/min (Nov 2018 peak, Aug 2019 trough) still failed, through swapped order, slightly low readings, or a typo (0.79 for 0.89) that they noticed afterwards. The pivotal elements are the peak and trough, not the January ticks.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(top(area)[Jan 2018]) → READ(y)≈0.78 → FIND(top(area)[Jan 2020]) → READ(y)≈0.75 → RANGE(first, last) ?wrong:endpoints-not-extrema → ANSWER(v)` | 4 | 0 | 4 | “i found confusing if you only asked for the comparison of only january of both years or the comparison between the full two years” |
| `MAX({top(area)}, y)=peak(area)[Nov 2018] → [PROJ → yaxis] → READ(y)≈0.88-0.89 → MIN({top(area)}, y)=pt[Aug 2019] → [PROJ → yaxis] → READ(y)≈0.67-0.69 → ANSWER(v) ?wrong:entry/precision/order-error` | 3 | 0 | 3 | “In general I just looked for the high and low points of the charts and estimated the price” |

**Operations** (trials using it): `READ` 7, `PROJ` 4, `FIND` 4, `RANGE` 4, `MIN` 3, `MAX` 3, `FIX` 2, `SCAN` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `pt` 2/7, `xtick` 3/2, `yaxis` 1/3, `mark` 1/3, `xaxis` 0/1, `chart` 1/0, `question` 1/0, `area` 1/0

**Specific elements:** `pt[Jan 2020]` 4, `peak(area)[Nov 2018]` 3, `pt[Aug 2019 trough]` 3, `yaxis` 3, `pt[Jan 2018]` 3, `xtick[January 2018]` 3, `xtick[January 2020]` 2, `pt[lowest]` 1, `peak(area)` 1, `xaxis` 1, `xtick[*]` 1, `question` 1

## AC2Q4 · area(variant 2) · characterize_trend
> Over the first 6 months of 2019, the price of a pound of coffee beans was roughly ____________.'

n = 3 (correct 0), no process info: 0

**Reference:** `FIND({xtick Jan..Jun 2019}) → SCAN({top(area) Jan..Jun 2019}) → TREND(area, Jan-Jun 2019)=↓ → ANSWER(Falling)`

In two of the three trials the participant judged the trend correctly for the stretch they looked at, but that stretch was early 2018, which rises, instead of 2019. Year disambiguation on the x-axis (the year shows only under the January labels) is again the pivotal failure. Both drew an imagined rising trendline over the 2018 region. The third traced the correct falling 2019 segment and wrote 'steady decrease', yet answered 'Rising', which points to a response-entry error rather than a perceptual one.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(interval[2018]) ?wrong:wrong-year → LOOK(top(area)[early 2018]) → trendline → TREND=↑ → ANSWER(Rising)` | 2 | 0 | 2 | “rising figures on the chart indicated the rising trend in prices” |
| `FIND({xtick Jan..Jun 2019}) → PROJ(trace top(area)) → TREND=↓ → ANSWER(Rising) ?wrong:answer-contradicts-reasoning` | 1 | 0 | 1 | “the graph of  the shaded part has shown a steady decrease over the first six months of 2019” |

**Operations** (trials using it): `TREND` 3, `LOOK` 2, `FIND` 2, `PROJ` 1

**Elements** (kind: text / sketch): `trendline` 1/2, `xtick` 1/1, `mark` 1/1, `area` 1/0

**Specific elements:** `trendline` 1, `trendline[Jan-Jun 2018]` 1, `xtick[June 2018]` 1, `top(area)[rising figures]` 1, `trendline[Apr-Jul 2018]` 1, `top(area)[Jan-Jul 2019]` 1, `{xtick Jan..Jun 2019}` 1, `area` 1

## BCQ3 · bar · determine_range
> What is the range of the global internet speed?

n = 9 (correct 0), no process info: 0

**Reference:** `SCAN({bar[*]}) → MIN(h)=bar[Sri Lanka] → PROJ(top → yaxis) → READ≈12.6 → MAX(h)=bar[South Korea] → PROJ(top → yaxis) → READ≈98.9 → RANGE(12.6, 98.9)`

Most participants (6/9) answered with the y-axis extent (10/0 to 100) rather than the data range; circles on the 100 and 10 tick labels are the signature gesture. Only two actually found the shortest and tallest bars, and one of those rounded to ticks; one drew a 'typical' band (20-50). One trial gave the near-correct 12/99 but was still scored incorrect, possibly due to field order. The ambiguous term 'range' is pivotal.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(ytick[min], ytick[max]) → READ(axis extent) ?wrong:axis-extent-not-data-range` | 6 | 0 | 6 | “the internet speed axis has a range of 0 and 100” |
| `MAX(bar) → PROJ(→ yaxis) → MIN(bar) → PROJ(→ yaxis) → RANGE` | 2 | 0 | 2 | “I found highest and lowest bar” |
| `SCAN(bars) → GROUP/AVG(typical band) ?wrong:not-extrema` | 1 | 0 | 1 | “just check how many  country averaging on that number.” |

**Operations** (trials using it): `READ` 7, `PROJ` 3, `FIND` 3, `MIN` 2, `SCAN` 2, `MAX` 2, `LOOK` 2, `RANGE` 1, `FIX` 1, `KNOW` 1, `CONFUSED` 1, `MAP` 1, `GROUP` 1, `AVG` 1

**Elements** (kind: text / sketch): `yaxis` 4/4, `ytick` 2/5, `bar` 2/3, `chart` 2/0, `annot` 0/1, `grid` 0/1, `color` 1/0

**Specific elements:** `yaxis` 6, `ytick[10]` 5, `ytick[100]` 5, `top(bar[South Korea])` 2, `chart` 2, `bar[max]` 1, `top(bar[Sri Lanka])` 1, `bar[min]` 1, `annot[0 written below axis]` 1, `yaxis[bottom]` 1, `color` 1, `bar[Sri Lanka]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## BCQ4 · bar · count
> In how many countries  is the internet speed slower than Japan?

n = 2 (correct 0), no process info: 0

**Reference:** `FIND(bar[Japan] \| xtick) → PROJ(top(bar[Japan]) → threshold line) → COUNT({bar[*]} \| h < Japan)=6`

Both trials are wrong despite sound strategies: one drew a threshold line through Japan's top but miscounted (4), the other circled exactly the six shorter bars but submitted 13, having initially ignored 'Japan' and counted all other countries. A drawn threshold line at Japan's height is the natural aid; the errors are in counting and task reading.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(bar[Japan]) → PROJ(threshold line) → COUNT(below) ?wrong:miscount` | 1 | 0 | 1 | “number of countries below the line, although i said its mistake.” |
| `FIND(bar[Japan]) → CMP(each < Japan) → COUNT=6 marked → ANSWER(13) ?wrong:misread-question` | 1 | 0 | 1 | “I made a mistake with counting because I missed the word Japan.” |

**Operations** (trials using it): `FIND` 2, `COUNT` 2, `PROJ` 1, `CMP` 1

**Elements** (kind: text / sketch): `bar` 1/2, `line` 1/0

**Specific elements:** `{bar[*]}` 1, `line` 1, `top(bar[Japan])` 1, `bar[Japan]` 1, `top(bar[Malaysia])` 1, `top(bar[India])` 1, `top(bar[Vietnam])` 1, `top(bar[Indonesia])` 1, `top(bar[Thailand])` 1, `top(bar[Sri Lanka])` 1, `bar[*]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## BuCQ2 · bubble · determine_range
> What is the range of metro system lengths  in the data shown in this chart?

n = 22 (correct 0), no process info: 0

**Reference:** `ARGMAX({bubble[*]}, y)=bubble[N.Y.C] → PROJ(center(bubble[N.Y.C]) → yaxis) → READ(y)≈458 → ARGMIN({bubble[*]}, y)=bubble[Mexico City] → PROJ(center(bubble[Mexico City]) → yaxis) → READ(y)≈163 → RANGE(163,458) → ANSWER(163–458)`

The dominant strategy (16/22) was to read the y-axis end ticks (500 and 150) as the data range: the sketches overwhelmingly circle or trace the axis limits rather than any bubble, so the axis extent was confused with the data extent. Only 4 participants projected from the extreme bubbles (N.Y.C top, Mexico City bottom) to the y-axis, and one picked the right extremes but the wrong axis (stations). Note that all 22 trials are scored 0, including the data-extent answers 160–460 / 170–460 that fall within tolerance; this looks like a lower/upper field-order issue in the scoring (one participant flags the inverted labels), so accuracy here is unreliable.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `READ(ytick[max])=500 → READ(ytick[min])=150 → RANGE(150,500) ?wrong:axis-extent-not-data-extent  [axis end-ticks taken as data range; via LOOK(yaxis)/LOOK(ytitle)/GIST]` | 14 | 0 | 14 | “I just looked at the y axis” |
| `ARGMAX/ARGMIN({bubble[*]}, y)=N.Y.C/Mexico City → PROJ(→ yaxis) → READ(y)≈460/≈160 → RANGE(160,460)  [data extent; scored 0 in data]` | 3 | 0 | 3 | “I have only looked at the y axis and selected the lowest and the highest point.” |
| `READ(yaxis extent) (traced whole axis) → RANGE(150,500) ?wrong:axis-extent-not-data-extent` | 2 | 0 | 2 | “we just read the y axis” |
| `ANSWER(150–500) ?wrong:axis-extent → FIX(→ data extent via PROJ(N.Y.C, Mexico City → yaxis)) → RANGE(155,455)` | 1 | 0 | 1 | “actually i made a mistake its between 155 and 455” |
| `FIND(bubble[Shanghai], bubble[Mexico City]) → PROJ(→ xaxis) → READ(x)≈750/≈200 ?wrong:wrong-axis(stations-not-length) → RANGE(200,750)` | 1 | 0 | 1 | “I looked at the number of stations” |
| `∅-ish: RANGE(150,500)? ?wrong → CONFUSED(lower vs upper)` | 1 | 0 | 1 | “sorry, I made mistakes in identifying lower and upper range” |

**Operations** (trials using it): `RANGE` 22, `READ` 21, `LOOK` 11, `PROJ` 5, `MAX` 4, `ARGMIN` 4, `ARGMAX` 4, `CONFUSED` 3, `GIST` 2, `KNOW` 1, `DOUBT` 1, `FIND` 1, `FIX` 1

**Elements** (kind: text / sketch): `yaxis` 8/9, `ytick` 1/13, `ytitle` 4/3, `bubble` 0/5, `chart` 3/0, `pt` 2/0, `xtitle` 2/0, `xtick` 0/1, `label` 1/0, `grid` 0/1

**Specific elements:** `yaxis` 13, `ytick[500]` 13, `ytick[150]` 13, `bubble[Mexico City]` 5, `ytitle` 5, `bubble[N.Y.C]` 4, `chart` 3, `xtitle` 2, `pt[lowest]` 2, `bubble[Shanghai]` 1, `xtick[750]` 1, `xtick[200]` 1

**New symbols:** `READ(yaxis extent)`: READ(yaxis extent)=a..b — reading the axis span itself (first/last tick) as a value pair, typically shown by tracing the whole axis

## BuCQ3 · bubble · make_comparison
> Tokyo has a bigger ridership than Guangzhow. True or False?

n = 40 (correct 37), no process info: 0

**Reference:** `MAP(size(bubble) → ridership \| legend) → FIND(bubble[Tokyo] \| label[Tokyo]) → FIND(bubble[Guangzhow] \| label[Guangzhow]) → CMPvis(size(bubble[Tokyo]) > size(bubble[Guangzhow])) → (optional READ via legend: ≈3.5 vs ≈3.0) → ANSWER(True)`

Nearly everyone (37/40) succeeded by comparing the two bubbles directly; the sketch is mostly two circles on Tokyo and Guangzhow. About a quarter went further and anchored each bubble to a legend circle (lines or arrows from Tokyo to 3.5 and Guangzhow to 3.0), turning the visual comparison into a value comparison. The pivotal elements are size(bubble) and the size legend. The 3 errors are not perceptual: one participant self-reported a misclick, one wrote a correct comparison but answered False, and one projected the bubbles to the x/y position axes instead of using size.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(bubble[Tokyo]) → FIND(bubble[Guangzhow]) → CMPvis(size(Tokyo) > size(Guangzhow)) → ANSWER(True)  [direct size comparison, no legend]` | 14 | 14 | 0 | “Size of tokyo circle is bigger than of guangzhow circle” |
| `MAP(size(bubble) → ridership \| legend) / LOOK(legend) → CMPvis(size(Tokyo) > size(Guangzhow)) → ANSWER(True)` | 12 | 12 | 0 | “The key helped find the answer - it showed that the bigger the circle, the bigger the ridership.” |
| `FIND(bubble) → READ(size \| legend[3.5])≈3.5 (Tokyo), READ(size \| legend[3.0])≈3.0 (Guangzhow) → CMP(3.5 > 3.0) → ANSWER(True)` | 10 | 10 | 0 | “The Toyko ridership is 3.5 and Guangzhow is 3.0” |
| `FIND both → PROJ(→ xaxis/yaxis) → MAP(size → ridership) → CMPvis → ANSWER(True)  [detour via position axes]` | 1 | 1 | 0 | “drawing on the graph will make you establish the number of stations of Tokyo and Guangzhou, but the size of the circle enabled me to identify the bigger ridership” |
| `FIND both → PROJ(→ xaxis, yaxis) → ANSWER(False) ?wrong:used-position-not-size` | 1 | 0 | 1 | “nothing was confusing” |
| `CMPvis(size(Guangzhow) < size(Tokyo)) → ANSWER(False) ?wrong:response-contradicts-own-comparison` | 1 | 0 | 1 | “the sixe of guangzhow is smaller than tokyo” |
| `LOOK(legend) → ANSWER(False) ?wrong:misclick` | 1 | 0 | 1 | “Actually I wanted to click "True" but I missclicked!” |

**Operations** (trials using it): `FIND` 34, `CMPvis` 29, `READ` 10, `MAP` 9, `LOOK` 9, `CMP` 9, `PROJ` 2, `CONFUSED` 1

**Elements** (kind: text / sketch): `bubble` 30/36, `legend` 7/18, `yaxis` 0/2, `chart` 2/0, `xtick` 0/1, `xaxis` 0/1, `label` 0/1, `xtitle` 1/0

**Specific elements:** `bubble[Tokyo]` 34, `bubble[Guangzhow]` 33, `size(bubble[Tokyo])` 12, `legend` 12, `legend[3.0]` 10, `size(bubble[*])` 9, `legend[3.5]` 9, `top(bubble[Tokyo])` 3, `size(bubble[Guangzhow])` 2, `yaxis` 2, `chart` 2, `bottom(bubble[Tokyo])` 2

**New symbols:** `area(m)`: mark part: the 2-D area of a mark, used when a participant says a bubble takes up more space; `legend[v]`: a specific legend entry, here a reference circle of the size legend (legend[3.5], legend[3.0], legend[2.5])

## BuCQ4 · bubble · find_correlation
> In general, the ridership of the metro system increases as the number of stations increases. True or False?

n = 39 (correct 26), no process info: 0

**Reference:** `MAP(size(bubble) → ridership \| legend) → MAP(x → stations) → SCAN({bubble[*]} along xaxis) → CORR(x, size(bubble)) ≈ 0 (e.g. OUTLIER: bubble[Beijing] high-x small; bubble[Tokyo] low-x largest) → ANSWER(False)`

This item requires relating a position channel (x = stations) to a size channel (ridership). The successful path was usually a counterexample: Beijing (far right, tiny) and Tokyo (left, largest) are the pivotal bubbles, often marked by dropping vertical lines from the bubbles to the x-axis. A smaller group scanned along x and reported no pattern. Errors came from prior-knowledge reasoning, perceiving an upward trend while dismissing exceptions, tracing a position trendline (length against stations) instead of using size, or deciding that no relation meant the question was unanswerable. Two participants reasoned correctly but said they mis-clicked True.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(counterexample: bubble high-x & small, e.g. Beijing / bubble low-x & large, e.g. Tokyo) → PROJ(→ xaxis) → CMP(size vs x) → CORR≠+ → ANSWER(False)` | 16 | 16 | 0 | “Beijing has a small bubble and is far to the right, whereas Tokyo is closer to the left (low number of stations) yet has a large bubble” |
| `SCAN({bubble[*]} along xaxis) → TREND(size, x)=~/↓ → CORR=0 → ANSWER(False)` | 6 | 6 | 0 | “there is no relation between this two, its very uneven” |
| `SCAN/GROUP → CORR unclear → DOUBT → ANSWER(Not sure / Impossible) ?wrong:no-relation-read-as-unanswerable` | 3 | 0 | 3 | “The ridership, I think does not have a patterns, that is why I am not sure” |
| `sketch-only: FIND/PROJ a few bubbles (→ xaxis or → legend) → ANSWER(False)` | 3 | 3 | 0 | “(no process in text)” |
| `∅/CONFUSED → ANSWER(Not sure)` | 3 | 0 | 3 | “I'm a bit confused by this representation” |
| `GROUP({bubble: same x}) → CMPvis(size differs at same x) → CORR≠+` | 2 | 1 | 1 | “Cities close together in number of stations but with great differences in ridership indicate that the affirmation is not true.” |
| `SCAN → TREND(size, x)≠↑ → ANSWER(True) ?wrong:response-contradicts-reasoning(self-reported)` | 2 | 0 | 2 | “I just realizeth the answer should be false - size of circles does not get bigger the higher the number of stations, my bad.” |
| `GIST/GROUP → TREND(size, x)=↑ ?wrong:perceived-positive-trend (exceptions dismissed) → ANSWER(True)` | 2 | 0 | 2 | “There area  few exceptions, but yeah, in general it seems like the ridership of the metro system increases” |
| `KNOW(more stations → more riders) ?wrong:prior-belief → ANSWER(True)` | 1 | 0 | 1 | “the more stations you have the more people you can reach hence making the number of riders to increase” |
| `LOOK(trendline through bubble positions) ?wrong:position-trend-not-size → DOUBT → ANSWER(Not sure)` | 1 | 0 | 1 | “I wasn't quite sure of my answer” |

**Operations** (trials using it): `CORR` 23, `FIND` 22, `PROJ` 12, `CMP` 12, `SCAN` 11, `TREND` 7, `READ` 6, `ARGMAX` 5, `GROUP` 5, `CMPvis` 5, `CONFUSED` 5, `DOUBT` 4, `KNOW` 3, `LOOK` 2, `ARGMIN` 2, `MAP` 1, `GIST` 1, `OUTLIER` 1

**Elements** (kind: text / sketch): `bubble` 24/32, `xaxis` 15/14, `legend` 1/3, `xtick` 1/2, `yaxis` 0/3, `region` 0/2, `trendline` 0/1, `grid` 0/1, `chart` 1/0, `xtitle` 0/1

**Specific elements:** `xaxis` 24, `bubble[Tokyo]` 22, `bubble[Beijing]` 19, `size(bubble[*])` 11, `bubble[N.Y.C]` 11, `bubble[London]` 9, `bubble[Paris]` 8, `bubble[Seoul]` 7, `bubble[Guangzhow]` 7, `bubble[Shanghai]` 6, `bubble[Mexico City]` 5, `bubble[Delhi]` 4

**New symbols:** `trendline`: (spec) used for a line the participant draws through bubble positions; `region[quadrants]`: a partition of the plot into regions by drawn cross-hair lines

## BuCQ5 · bubble · compute_derived_value
> The average metro system in this chart has approximately 300 stations 200km in length

n = 40 (correct 15), no process info: 0

**Reference:** `SCAN({bubble[*]}) → READ(x) per bubble (≈200…740) → AVG(x)≈440 → READ(y) per bubble → AVG(y)≈310 → CMP((440,310) vs (300,200)) → ANSWER(False)  [shortcut: COUNT({bubble: x>300 ∧ y>200}) = most, so the mean is above both targets]`

This item asks for the mean of 11 points, and the chart shows no average, so a quarter of participants said it was impossible or unclear. The most common sketch is a cross-hair to the target point (300 stations, 200 km). From there people split: those who noticed the bubbles sit mostly above and to the right of it said False, while those who looked for a bubble at exactly that point and found none answered Not sure or Impossible. Correct reasoners counted bubbles beyond the thresholds or estimated and averaged x-values (one wrote out 4440/11 = 444). Wrong True answers came from substitutes for the mean: majority counts, a diagonal centre line, the midrange of extremes, or a single bubble near the target (Tokyo).

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `∅/CONFUSED/GIST("no average shown") → ANSWER(Impossible / Not sure) ?wrong:average-is-estimable` | 10 | 0 | 10 | “I couldn't find an answer because I don't see the average shown in this graphic” |
| `FIND(pt[300,200]) → PROJ → CMP(no bubble at target) → ANSWER(Not sure/Impossible) ?wrong:needs-centroid-not-matching-point` | 6 | 0 | 6 | “the average 300 stations 200 km length does not coincide with any location.” |
| `FIND(pt[300,200]) → PROJ(from x=300 and y=200 ticks) → CMP(no/few bubbles near target) → ANSWER(False)` | 5 | 5 | 0 | “Just by locating where 300 stations and 200km are in the chart, you can see none of them are close to that range.” |
| `FIND(threshold x=300 / y=200) → COUNT({bubble above}) = most → CMP(mean > target) → ANSWER(False)` | 5 | 5 | 0 | “9 out of 11 cities has more than 200km system length, therefore this cannot be the average.” |
| `READ(x) for every bubble → SUM/COUNT → AVG≈444 → CMP(≠300) → ANSWER(False)` | 2 | 2 | 0 | “I calculated c. 445 which was a fair bit more than 300” |
| `COUNT(above/below 300)=6/5 → ANSWER(True) ?wrong:majority-or-split-count-not-mean` | 2 | 0 | 2 | “6 of the 11  metro systems are above 300” |
| `KNOW(centre line)/AVG(min,max) → READ(centre)≈target ?wrong:centre-line-or-midrange-not-mean → ANSWER(True)` | 2 | 0 | 2 | “From my memory of maths you should draw a centre line and then the cluster will show you the average” |
| `FIND(single bubble near target, e.g. Tokyo / mid-y bubble) → ANSWER(True) ?wrong:single-bubble-as-average` | 2 | 0 | 2 | “I paid attention to the blue circle at the half of y axis” |
| `MAX(x), MAX(y) extents ≈750/460 ?wrong:extremes-not-mean → ANSWER(False); or sketch-only PROJ of one bubble` | 2 | 2 | 0 | “There are about 750 stations and the total length of 460km” |
| `GROUP → FIND(visual centre via crossed lines) → AVG≈(375,265) → CMP → ANSWER(False)` | 1 | 1 | 0 | “The crossed lines, for me, simbolized the average of both parameters” |
| `AVG(two largest bubbles Tokyo, Shanghai)≈(550,325) ?wrong → DOUBT → ANSWER(Not sure)` | 1 | 0 | 1 | “I think it would be somewhere between Tokyo and Shanghai values since they are the biggest.” |
| `FIND(grid[x=300]) → SCAN → AVG(x)>300 → DOUBT → ANSWER(Not sure)` | 1 | 0 | 1 | “The average seems to be more than 300 sations.” |
| `sketch PROJ of a point → ANSWER(True) ?wrong:response-contradicts-belief(self-reported)` | 1 | 0 | 1 | “I think the correct answer is false.” |

**Operations** (trials using it): `FIND` 28, `CMP` 22, `PROJ` 20, `COUNT` 8, `AVG` 8, `SCAN` 6, `CONFUSED` 6, `READ` 5, `KNOW` 4, `GIST` 3, `GROUP` 2, `DOUBT` 2, `SUM` 1, `LOOK` 1, `ARGMAX` 1, `MAX` 1

**Elements** (kind: text / sketch): `bubble` 14/14, `pt` 3/16, `grid` 0/17, `annot` 4/8, `xaxis` 2/5, `yaxis` 2/5, `xtick` 4/2, `ytick` 3/2, `cluster` 1/1, `trendline` 1/1, `question` 2/0, `region` 0/2, `chart` 1/0, `ytitle` 1/0, `xtitle` 1/0

**Specific elements:** `grid[x=300]` 14, `grid[y=200]` 13, `pt[300,200]` 13, `{bubble[*]}` 9, `yaxis` 7, `xaxis` 6, `annot[?]` 6, `bubble[Tokyo]` 4, `xtick[300]` 4, `bubble[Mexico City]` 3, `ytick[200]` 3, `bubble[Shanghai]` 3

**New symbols:** `pt[x,y]`: a location in data space (not a mark), e.g. the target point pt[300,200] formed by projecting from two ticks; `annot[?]`: a question mark or other note written by the participant (used here for participant-written annotations); `region[x<a,y<b]`: a region of the plot defined by thresholds

## BuCQ6 · bubble · find_extremum
> Which city's metro system has the largest number of stations?

n = 7 (correct 0), no process info: 0

**Reference:** `MAP(x → stations \| xtitle) → SCAN({bubble[*]} along xaxis) → ARGMAX({bubble[*]}, x)=bubble[Shanghai] (≈740, just right of Beijing ≈725) → ANSWER(Shanghai)`

All 7 trials in this group are wrong, and 6 answered Tokyo: they took the largest bubble (the size channel, ridership) rather than the rightmost one (x = stations). Two participants caught this afterwards and circled Shanghai, explicitly naming the size-versus-numbers confusion. One used the wrong position axis (N.Y.C is highest on y = length). The pivotal elements are the x-axis title and the close pair Shanghai/Beijing at the right edge, which no wrong answer attended to. With only 7 trials, all incorrect, this sample shows error strategies and says nothing about how often the item is answered correctly.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `ARGMAX({bubble[*]}, size)=Tokyo ?wrong:size-channel-not-x-position → ANSWER(Tokyo)` | 3 | 0 | 3 | “Tokyo has the largest circle.” |
| `ARGMAX(size)=Tokyo ?wrong → ANSWER(Tokyo) → FIX(→ ARGMAX(x)=Shanghai)` | 2 | 0 | 2 | “I used my visualization instead of numbers.” |
| `ARGMAX({bubble[*]}, y)=N.Y.C ?wrong:wrong-axis → PROJ(→ yaxis, xaxis) → ANSWER(N.Y.C.)` | 1 | 0 | 1 | “drawing the lines to my answers” |
| `GUESS → ANSWER(Tokyo) ?wrong` | 1 | 0 | 1 | “I am not sure about this, I was just question” |

**Operations** (trials using it): `ARGMAX` 6, `FIX` 2, `PROJ` 1, `GUESS` 1

**Elements** (kind: text / sketch): `bubble` 3/6, `xtick` 1/0, `annot` 1/0, `yaxis` 0/1, `xaxis` 0/1

**Specific elements:** `bubble[Tokyo]` 3, `bubble[Shanghai]` 2, `size(bubble[max])` 1, `xaxis` 1, `yaxis` 1, `bubble[N.Y.C]` 1, `xtick[*]` 1, `bubble[Beijing]` 1, `size(bubble[*])` 1, `annot[numbers]` 1, `size(bubble[Tokyo])` 1, `bubble[Delhi]` 1

## CCQ2 · choropleth · retrieve_value
> What was the unemployment rate for Indiana (IN) in 2020?

n = 5 (correct 0), no process info: 0

**Reference:** `FIND(region[IN] \| label) → READ(color) → FIND(colorscale swatch matching color) → MAP(swatch → bin between labels 6% and 8%) → ANSWER(6-8%)`

All five participants matched Indiana to the correct (3rd) legend swatch, as their circles/X marks/lines show, but then mis-assigned the bin: the legend labels sit at swatch boundaries, so the swatch can be read as '4-6' or '6-8'. Two answered 4-6, two explicitly declared it undecidable, one answered 8-10. The pivotal element is the colorscale label alignment, not the colour match itself.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(region[IN]) → READ(color) → FIND/PROJ(→ colorscale swatch) → MAP(swatch → 4-6%) ?wrong:label-misalignment` | 2 | 0 | 2 | “By looking at the color I chose the closet one from the bar on the bottom” |
| `FIND(region[IN]) → MAP(swatch → 4-6\|6-8) → CONFUSED(bin labels) → ANSWER(impossible/not sure)` | 2 | 0 | 2 | “I could not determine from the drop-down list whether it is between 4-6% or 6-8%.” |
| `SCAN(chart)×3 → FIND(region[IN]) → FIND(swatch) → MAP ?wrong:8-10` | 1 | 0 | 1 | “had to search whole map three times and then missed the color” |

**Operations** (trials using it): `MAP` 5, `FIND` 5, `READ` 4, `CONFUSED` 2, `SCAN` 1, `CMP` 1, `PROJ` 1

**Elements** (kind: text / sketch): `colorscale` 3/4, `region` 1/5, `color` 4/0

**Specific elements:** `region[IN]` 5, `color` 4, `colorscale[6-8 swatch]` 3, `colorscale` 3, `region[IL]` 1, `colorscale[6% boundary]` 1

**New symbols:** `colorscale[swatch]`: one discrete swatch of a binned colour legend; `ANSWER(v)`: final submitted response

## HCQ1 · histogram · compute_derived_value
> How many people have traveled a distance between 20km and 40km?

n = 8 (correct 0), no process info: 0

**Reference:** `FIND({bin[20-30],bin[30-40]} \| xtick 20..40) → PROJ(top → yaxis) → READ(y)≈215 → PROJ(top → yaxis) → READ(y)≈247 → SUM≈462`

All 8 wrong. The dominant error (3/8, answer 635) is a bin-to-tick mismatch: with ticks at bin edges, participants took '20, 30 and 40' as three bars and added the 10-20 bin too. Others picked the right two bins but under/over-estimated the tops (440, 475), substituted the 10-20 bin (407), read only the tallest bin (250), or confused the axes entirely (80). Edge-labelled x ticks are the pivotal element.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(3 bins @ xticks 20,30,40) ?wrong:included-10-20 → PROJ(top → yaxis)×3 → READ×3 → SUM=635` | 3 | 0 | 3 | “I just added the number of people in 20, 30 and 40kms range” |
| `FIND({bin[20-30],bin[30-40]}) → READ(top)×2 → SUM ?wrong:estimation` | 2 | 0 | 2 | “added the two numbers tof=gether” |
| `PROJ(top(bin[10-20])) ?wrong:wrong-bin → PROJ(top(bin[30-40])) → SUM` | 1 | 0 | 1 | “Look closely at the graph to see the number of passengers” |
| `FIND(bin[30-40]) → PROJ(top → yaxis) → READ≈250 ?wrong:single-bin` | 1 | 0 | 1 | “it was so easy to find this one.” |
| `FIND(xtick[80]) → PROJ(→ ytick[40]) ?wrong:axis-confusion` | 1 | 0 | 1 | “THE GRAPHIC IS CLEAR WITH COLORS IT WAS CLEAR” |

**Operations** (trials using it): `READ` 7, `FIND` 7, `SUM` 6, `PROJ` 5, `DOUBT` 1, `SCAN` 1

**Elements** (kind: text / sketch): `bin` 4/7, `yaxis` 0/4, `xtick` 1/1, `ytick` 0/2, `grid` 1/0, `chart` 1/0, `color` 1/0

**Specific elements:** `bin[30-40]` 4, `yaxis` 4, `bin[20-30]` 3, `bin[10-20]` 3, `top(bin[30-40])` 3, `bin` 2, `top(bin[20-30])` 2, `bin[*]` 1, `grid` 1, `color` 1, `ytick[40]` 1, `xtick[80]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## HCQ2 · histogram · make_comparison
> More people have traveled the distance between 10 and 20 km than between 40 and 50 km. True or False?

n = 20 (correct 16), no process info: 0

**Reference:** `FIND(bin[10-20]) → FIND(bin[40-50]) → PROJ(top(bin[10-20]) → bin[40-50]) → CMPvis(height(bin[40-50]) > height(bin[10-20])) → ANSWER(False)`

The bars differ by only ~3 customers, so the dominant correct strategy (shown by sketches) is a horizontal reference line from one bar top to the other, often along the 180 gridline. Errors come from bin localisation with edge-labelled ticks (using 20-30 or 0-10 for '10-20') and from judging the bars 'the same' then answering True. Several correct answers rest on wrong bins (30-40, 50-60), so accuracy overstates the reading.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(bin[10-20]) → FIND(bin[40-50]) → PROJ(top ↔ top) reference line → CMPvis(40-50 > 10-20) → False` | 10 | 10 | 0 | “By drawing a line we can tell that 40 and 50 km is slightly larger than 10 and 20 km.” |
| `LOOK(top(bin[10-20])) → LOOK(top(bin[40-50])) → CMPvis (marks/gridline gap) → False` | 3 | 3 | 0 | “The 40-50km is taller, because it needs less to reach 180” |
| `PROJ(top ↔ top) → CMP(≈ same) → ANSWER(False \| True)` | 2 | 1 | 1 | “the numbers confused me, therefore i messed up my answer and later realized that its the same” |
| `FIND(bin[20-30]) ?wrong:wrong-bin → READ/PROJ(top) → CMP(> bin[40-50]) → True` | 2 | 0 | 2 | “the 20 to 30 has around 217 costumers and the 40 to 50 has around 179 costumers” |
| `FIND(bin[0-10]) ?wrong:tick-bin-misalignment → CONFUSED(xaxis) → True` | 1 | 0 | 1 | “The x-axis are confusing!” |
| `PROJ(top(bin[30-40])) ?wrong:wrong-bin → PROJ(top(bin[10-20])) → ARGMAX → False` | 1 | 1 | 0 | “According to the graph, the comparison shows that 30 to 40 km is most popular.” |
| `FIND(xtick[50]) → PROJ(→ yaxis)≈100 ?wrong:wrong-bin → False` | 1 | 1 | 0 | “THE GRAPHIC IS CLEAR WITH COLORS IT WAS CLEAR” |

**Operations** (trials using it): `PROJ` 15, `CMPvis` 13, `FIND` 12, `LOOK` 5, `CMP` 5, `CONFUSED` 2, `READ` 2, `ARGMAX` 1, `GIST` 1

**Elements** (kind: text / sketch): `bin` 12/20, `yaxis` 1/8, `xtick` 2/4, `grid` 2/2, `chart` 2/0, `xaxis` 1/0, `color` 1/0

**Specific elements:** `top(bin[10-20])` 16, `top(bin[40-50])` 14, `bin[40-50]` 9, `yaxis` 8, `bin[10-20]` 5, `xtick[10]` 4, `xtick[50]` 4, `grid[y=180]` 3, `bin[0-10]` 2, `top(bin[20-30])` 2, `xtick[20]` 2, `xtick[40]` 2

**New symbols:** `PROJ(a ↔ b)`: horizontal reference line drawn between two mark tops for direct comparison; `ANSWER(v)`: final submitted response

## HCQ3 · histogram · find_extremum
> What is the most common distance customers have travelled?

n = 3 (correct 0), no process info: 0

**Reference:** `SCAN({bin[*]}) → ARGMAX({bin[*]}, h)=bin[30-40] → FIND(xtick[30], xtick[40]) → ANSWER(30-40 km)`

All three trials are wrong and none performs the ARGMAX: one equates 'most common distance' with the largest x value (110), one reasons that the common distance is the one everybody covered and takes the lowest bar (ARGMIN), and one projects a mid-height bar. The question wording ('most common distance') and the edge-labelled x axis are the pivotal stumbling blocks.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `KNOW(misread 'most common') → SCAN({bin}) → ARGMIN(h) ?wrong:argmin-not-argmax` | 1 | 0 | 1 | “It had to be the lowest distance for all of them to have covered” |
| `FIND(xtick[max]) ?wrong:MAP(largest x → most common)` | 1 | 0 | 1 | “I used the graph to find my answer.” |
| `FIND(xtick[70]) → PROJ(top(bin[60-70]) → yaxis) ?wrong:non-max-bin` | 1 | 0 | 1 | “THE GRAPHIC IS CLEAR WITH COLORS IT WAS CLEAR” |

**Operations** (trials using it): `FIND` 2, `PROJ` 1, `MAP` 1, `KNOW` 1, `SCAN` 1, `ARGMIN` 1

**Elements** (kind: text / sketch): `bin` 1/2, `xtick` 0/2, `color` 1/0, `yaxis` 0/1, `chart` 1/0

**Specific elements:** `color` 1, `yaxis` 1, `xtick[70]` 1, `top(bin[60-70])` 1, `xtick[110]` 1, `chart` 1, `{bin[*]}` 1, `bin[lowest]` 1, `top(bin[90-100])` 1

**New symbols:** `ANSWER(v)`: final submitted response

## HC2Q1 · histogram(variant 2) · compute_derived_value
> How many people have traveled a distance between 20km and 40km?

n = 6 (correct 0), no process info: 0

**Reference:** `FIND({bin[20-30],bin[30-40]} \| xtick labels) → PROJ(top → yaxis) → READ≈215 → PROJ(top → yaxis) → READ≈247 → SUM≈462`

With range-labelled ticks almost everyone picked the right two bins (contrast HCQ1), so errors move to reading and arithmetic: underestimated tops (420, 453), odd sums (269), or no sum at all (260, 230). One participant explicitly believed bins might be cumulative and averaged instead of adding; another still added 10-20. Precise reading of tops between 20-unit gridlines is the pivotal step.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND({bin[20-30],bin[30-40]}) → READ/PROJ(top)×2 → SUM ?wrong:read-or-arithmetic` | 3 | 0 | 3 | “I just markeked the highest Distance between  20-40 Kn and at the highs” |
| `FIND(xtick labels) → PROJ(→ yaxis) → READ(range 200-240) ?wrong:no-sum` | 1 | 0 | 1 | “Took the two bars that correspond to this and estimated volume from left hand axis” |
| `FIND(2 bins) → MAP(bins cumulative) ?wrong → AVG ?wrong:no-sum` | 1 | 0 | 1 | “maybe the people of the 20-30 bar are included in the 30-40 bar” |
| `FIND(3 bins incl. 10-20) ?wrong → READ×3 → SUM → CONFUSED(boundaries)` | 1 | 0 | 1 | “a little confusing wheter i should add the people who walked a little less or a little more” |

**Operations** (trials using it): `FIND` 6, `READ` 4, `SUM` 4, `PROJ` 2, `LOOK` 1, `DOUBT` 1, `CONFUSED` 1, `MAP` 1, `AVG` 1

**Elements** (kind: text / sketch): `bin` 5/5, `xtick` 0/3, `yaxis` 1/1, `ytick` 1/1

**Specific elements:** `xtick[30-40]` 3, `xtick[20-30]` 3, `top(bin[20-30])` 3, `top(bin[30-40])` 3, `bin[20-30]` 2, `bin[30-40]` 2, `yaxis` 2, `bin[20..40]` 2, `bin` 1, `ytick[200..240]` 1, `ytick` 1, `top(bin[10-20])` 1

**New symbols:** `ANSWER(v)`: final submitted response

## HC2Q2 · histogram(variant 2) · make_comparison
> More people have traveled the distance between 10 and 20 km than between 40 and 50 km. True or False?

n = 21 (correct 20), no process info: 0

**Reference:** `FIND(bin[10-20] \| xtick label) → FIND(bin[40-50] \| xtick label) → PROJ(top(bin[10-20]) → bin[40-50]) → CMPvis(height(bin[40-50]) > height(bin[10-20])) → ANSWER(False)`

20/21 correct. With range labels the bins are found easily, and the near-tie (~176 vs ~179) is settled mostly by drawing a horizontal reference line from one bar top to the other or to the 180 gridline. A minority just marked both tops and compared. The only error came from marking the 20-30 bar instead of 10-20, and one correct answer was hedged as 'equal or slightly less'.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(bin[10-20]) → FIND(bin[40-50]) → PROJ(top ↔ top / to y-axis 180) reference line → CMPvis(40-50 > 10-20) → False` | 15 | 15 | 0 | “I just drew a line across from the highest of 10-20Km to 40-50Kn to see if it higher or lower” |
| `LOOK(top(bin[10-20])) → LOOK(top(bin[40-50])) (marks/boxes/arrows) → CMPvis → False` | 4 | 4 | 0 | “40-50 bar appears to be closer to the 180 line than the 10-20 bar” |
| `PROJ(top ↔ top) → CMP(≈) → DOUBT → False` | 1 | 1 | 0 | “It is equal or slightly less. hard to tell” |
| `FIND(bin[20-30]) ?wrong:wrong-bin → LOOK(tops) → CMP(212 > 175) → True` | 1 | 0 | 1 | “find the mark on each statement, see which was higher” |

**Operations** (trials using it): `CMPvis` 18, `PROJ` 16, `FIND` 14, `LOOK` 6, `CMP` 4, `DOUBT` 1, `READ` 1

**Elements** (kind: text / sketch): `bin` 15/21, `yaxis` 1/11, `xtick` 1/3, `ytick` 1/2, `grid` 1/1, `annot` 1/0, `chart` 1/0, `line` 1/0

**Specific elements:** `top(bin[10-20])` 19, `top(bin[40-50])` 18, `bin[40-50]` 16, `yaxis` 11, `bin[10-20]` 8, `xtick[40-50]` 3, `xtick[10-20]` 2, `ytick[180]` 2, `bin` 2, `grid[y=180]` 1, `top(bin[20-30])` 1, `annot[statement]` 1

**New symbols:** `PROJ(a ↔ b)`: horizontal reference line drawn between two mark tops for direct comparison; `ANSWER(v)`: final submitted response

## HC2Q3 · histogram(variant 2) · find_extremum
> What is the most common distance customers have travelled?

n = 2 (correct 0), no process info: 0

**Reference:** `SCAN({bin[*]}) → ARGMAX({bin[*]}, h)=bin[30-40] → READ(xtick label)=30-40 → ANSWER(30-40 km)`

Both trials fail before any extremum search: one reads the axis as a sequence starting from zero and answers the first bin, the other draws a question mark over the tallest bars and declares it unanswerable. The interpretation of 'most common distance' as 'tallest bin' is the missing link.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(xtick[0-10]) → SCAN(xaxis) → MAP(first bin) ?wrong:not-argmax` | 1 | 0 | 1 | “You start moving from Zero to high” |
| `LOOK(tallest bins) → CONFUSED(task) → impossible` | 1 | 0 | 1 | “Not sure how to answer” |

**Operations** (trials using it): `FIND` 1, `MAP` 1, `SCAN` 1, `LOOK` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `xaxis` 1/1, `bin` 0/1, `xtick` 0/1

**Specific elements:** `xtick[0-10]` 1, `xaxis` 1, `bin[40-50]` 1, `bin[30-40]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## LCQ1 · line · retrieve_value
> What was the price of a barrel of oil in February 2020?

n = 1 (correct 0), no process info: 0

**Reference:** `FIND(xtick[Feb]) → FIND(pt[Feb]) → PROJ(pt[Feb] → yaxis) → READ(pt[Feb], y)≈50.5 → ANSWER(≈50.5)`

Only one (incorrect) trial in this group. The participant's sketch shows a textbook x-tick→point→y-axis projection landing at ~51, yet the submitted 29 matches the March point, suggesting a response-entry slip or neighbour-point confusion rather than a reading-strategy failure.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(xtick[Feb]) → FIND(pt[Feb]) → PROJ(pt → yaxis) → READ(y)≈51 → ANSWER(29) ?wrong:entry-slip/neighbour-point` | 1 | 0 | 1 | “Firstly I found the month and than the blue dot which was above of it.” |

**Operations** (trials using it): `READ` 1, `PROJ` 1, `FIND` 1

**Elements** (kind: text / sketch): `xtick` 1/1, `pt` 1/1, `yaxis` 1/1, `ytick` 0/1

**Specific elements:** `pt[Feb]` 1, `ytick[50]` 1, `xtick[Feb]` 1, `yaxis` 1

**New symbols:** `ANSWER(v)`: the final response the participant submitted (used to show mismatch with read value)

## LCQ3 · line · determine_range
> What was the price range of a barrel of oil in 2020?

n = 4 (correct 0), no process info: 0

**Reference:** `SCAN({pt[*]}) → MIN(y)=pt[Apr] → READ(y)≈16.5 → MAX(y)=pt[Jan] → READ(y)≈57.5 → RANGE(16.5, 57.5)`

All four trials are wrong, mostly not because of the extremum search (three of four correctly find Jan and Apr) but because of reading/entry: the max is under-read (52), rounded up to the axis top (60) or misread (67.5), and the answer fields seem to have been filled max-first. One participant circled the endpoints (Jan, Dec) instead of the min, confusing 'range' with start-to-end values.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `MIN({pt},y) → MAX({pt},y) → READ(max)?wrong → READ(min) → ANSWER(max/min)` | 2 | 0 | 2 | “Lowest point and highest point” |
| `MAX → MIN → PROJ(pt[Apr] → yaxis) → READ(ytick) rounded ?wrong:rounded-to-ticks → ANSWER(60/15)` | 1 | 0 | 1 | “the left sided numbers” |
| `LOOK(pt[Jan]) → LOOK(pt[Dec]) → CONFUSED(scope) → READ(endpoints) ?wrong:endpoints-not-extrema` | 1 | 0 | 1 | “got confused with whether the lower was for the whole year or quaterly” |

**Operations** (trials using it): `READ` 4, `MIN` 3, `MAX` 3, `PROJ` 1, `LOOK` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `pt` 2/4, `yaxis` 0/1, `ytick` 1/0

**Specific elements:** `pt[Jan]` 4, `pt[Apr]` 3, `pt[min]` 2, `pt[max]` 2, `yaxis` 1, `ytick` 1, `pt[Dec]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## LCQ4 · line · characterize_trend
> Over the course of the first quarter of 2020, the price of a barrel of oil was ______.

n = 3 (correct 0), no process info: 0

**Reference:** `FIND(xtick[Jan..Mar]) → SCAN(line[Jan..Mar]) → TREND(line, Q1)=↓ → ANSWER(falling)`

All three trials fail on the temporal scope 'first quarter', not on trend perception: one considered the whole year (flat later, falling earlier), one traced Jan–Jun so the V-shape read as 'unstable', and one correctly isolated a falling segment but reports a misclick. Mapping 'first quarter' to Jan–Mar ticks is the pivotal step.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `SCAN(line[whole year]) → TREND(late)=→, TREND(early)=↓ → DOUBT ?wrong:scope-not-Q1` | 1 | 0 | 1 | “I think it was constant in the late months but had a severe decrease in price in the earlier ones” |
| `SCAN(line[Jan..Jun]) ?wrong:scope-extended → TREND=~ ('unstable')` | 1 | 0 | 1 | “It wasn't rising nor was it falling , it was unstable.” |
| `FIND(line[Feb..Apr]) → TREND=↓ → ANSWER(impossible) ?wrong:misclick` | 1 | 0 | 1 | “i think i miss clicked ,the price was falling” |

**Operations** (trials using it): `TREND` 3, `SCAN` 2, `DOUBT` 1, `FIND` 1

**Elements** (kind: text / sketch): `line` 3/3, `pt` 0/1, `grid` 0/1

**Specific elements:** `line` 3, `grid[y=40]` 1, `line[late months]` 1, `line[early months]` 1, `pt[Mar]` 1, `line[Feb..Apr]` 1, `pt[Apr]` 1, `line[Jan..Jun]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## LCQ5 · line · compute_derived_value
> About how much did the price of a barrel of oil rise from April to August in 2020?

n = 9 (correct 0), no process info: 0

**Reference:** `FIND(pt[Apr]) → PROJ(→ yaxis) → READ(y)≈16.5 → FIND(pt[Aug]) → PROJ(→ yaxis) → READ(y)≈42.3 → DIFF(42.3,16.5)≈25.8`

Every trial is incorrect, yet most sketches show the correct double projection of the Apr and Aug points onto the y-axis (≈16 and ≈42); failures are arithmetic or entry slips (31, 1666, 30) that several participants self-report. Distinct errors include using the Dec point instead of Aug, ending the interval at Jul, and reporting the Aug level (41) instead of the rise. The y-axis projection of the two endpoints is the pivotal step; the subtraction is where it breaks.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `PROJ(pt[Apr] → yaxis) → READ≈16 → PROJ(pt[Aug] → yaxis) → READ≈42 → DIFF ?wrong:arithmetic` | 3 | 0 | 3 | “Counted wrong. Should have been 26.” |
| `READ(pt[Apr]) → READ(pt[Aug]) → DIFF ?wrong:value-or-entry` | 3 | 0 | 3 | “dolar amount of Aug - dolar amount of Apr” |
| `PROJ(pt[Apr]) → PROJ(pt[Dec]) ?wrong:wrong-endpoint → DIFF(46,16)=30` | 1 | 0 | 1 | “It increased 30 just by substracting 16 to 46” |
| `FIND(pt[Apr]) → SCAN(line) → FIND(pt[Aug]) → SUM ?wrong:addition` | 1 | 0 | 1 | “i just did a quick addition than i came to that answer” |
| `LOOK(line[Apr..Jul]) ?wrong:end-at-Jul → GUESS` | 1 | 0 | 1 | “look closely at the graph” |

**Operations** (trials using it): `DIFF` 7, `READ` 6, `PROJ` 4, `FIND` 3, `SCAN` 2, `SUM` 1, `GUESS` 1, `LOOK` 1, `DOUBT` 1

**Elements** (kind: text / sketch): `pt` 2/7, `yaxis` 2/4, `line` 0/3, `xaxis` 1/1, `xtick` 0/1, `chart` 1/0

**Specific elements:** `pt[Apr]` 7, `pt[Aug]` 6, `yaxis` 5, `line[Apr..Aug]` 2, `xaxis[Apr..Aug]` 1, `pt[Dec]` 1, `line[Apr..Jul]` 1, `chart` 1, `xtick[Apr]` 1, `xaxis` 1, `xtick[Aug]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## PCQ1 · pie · retrieve_value
> What is the approximate global smartphone market share (in %) of Samsung?

n = 6 (correct 0), no process info: 0

**Reference:** `FIND(slice[Samsung]) → READ(angle(slice[Samsung]))≈90° → RATIO(90°/360°) → PCT ≈25%`

All six trials are wrong, yet nearly every sketch correctly isolates Samsung as a right-angle quarter. The errors are in the angle-to-percent conversion: 90° reported as 90%, a right angle read as 50%, 'quarter' tangled with 45 degrees (44), or a half-of-half estimate (23) entered as 48. Pie chart failures here are conceptual (degrees vs. percent), not perceptual.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(slice[Samsung]) → READ(angle)=90° → MAP(angle → %) ?wrong:degree/percent-confusion` | 3 | 0 | 3 | “Which is 90% on the pie chart of the 360” |
| `FIND(slice[Samsung]) → LOOK/GIST(traced slice) → ANSWER(estimate) ?wrong` | 2 | 0 | 2 | “Look closely at the graph to see what the percentage is.” |
| `PROJ(diameter → halves 50%) → GROUP(Samsung+Others)=50% → RATIO(/2)≈23 → ANSWER(48) ?wrong:entry-slip` | 1 | 0 | 1 | “The line in the middle represent 50% on each side and when we devide the half that sunmsung and others share we can see we have more or less 23%” |

**Operations** (trials using it): `FIND` 5, `MAP` 4, `READ` 3, `PROJ` 2, `LOOK` 1, `GIST` 1, `GROUP` 1, `RATIO` 1

**Elements** (kind: text / sketch): `slice` 4/6, `chart` 2/3, `line` 1/0, `mark` 1/0

**Specific elements:** `slice[Samsung]` 4, `chart` 3, `edge(slice[Samsung])` 2, `angle(slice[Samsung])` 2, `center(chart)` 2, `angle` 1, `line[middle]` 1, `slice[Others]` 1

**New symbols:** `ANSWER(v)`: final submitted response

## PCQ2 · pie · find_extremum
> Which company has the largest global market share for smart phones?

n = 2 (correct 0), no process info: 0

**Reference:** `SCAN({slice[*]}) → ARGMAX({slice[company]}, angle) excluding slice[Others] → CMPvis(angle(Samsung) > angle(Others) or KNOW(Others ≠ company)) → ANSWER(Samsung)`

Both trials draw the same boundaries (vertical diameter plus Samsung/Others radius) and conclude the two quarters are visually tied. Neither uses the fact that 'Others' is not a company; one answers Others, the other gives up. The pivotal elements are the near-equal Samsung and Others slices and the semantic status of the Others label.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(Samsung) → FIND(Others) → PROJ(edges) → CMPvis(≈) → DOUBT/CONFUSED ?wrong:near-tie,ignored-Others-semantics` | 2 | 0 | 2 | “Samsung and others kinda share the same, visualization is not great” |

**Operations** (trials using it): `PROJ` 2, `FIND` 2, `CMPvis` 2, `DOUBT` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `slice` 2/2, `area` 1/0

**Specific elements:** `edge(slice[Samsung])` 2, `slice[Samsung]` 2, `slice[Others]` 2, `edge(slice[Others])` 2, `area` 1

**New symbols:** `ANSWER(v)`: final submitted response

## SAQ1 · stacked_area · retrieve_value
> What was the number of girls named 'Isla' in 2010 in the UK?

n = 36 (correct 0), no process info: 0

**Reference:** `FIND(band[Isla] \| legend[Isla]→color[purple]) → FIND(xtick[2010]) → PROJ(top(band[Isla])@2010 → yaxis) → READ(y)≈6600 → PROJ(bottom(band[Isla])=top(band[Amelia])@2010 → yaxis) → READ(y)≈4200 → SEG(6600 − 4200) ≈ 2400 → ANSWER(≈2400)`

Not a single participant subtracted the lower boundary: nearly everyone traced the 2010 tick up to the top edge of the purple band and across to the y-axis, reporting the cumulative ~6500 instead of the band thickness (~2400). The sketches are strikingly uniform L-shaped 'up-then-across' traces, which shows a line-chart reading schema applied to a stacked area. The minority errors were different targets: the top of the whole stack (Olivia, ~12000), the 2012 Isla peak (~10500), or the Amelia/Isla boundary (~4200). One participant explicitly knew the bands were stacked (P8) and another explicitly believed the band body was 'just aesthetics' (P15), yet both still read the top edge; the pivotal element, bottom(band[Isla]), was marked only once (P34) and never used in a subtraction.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(xtick[2010]) → PROJ(xtick[2010] → top(band[Isla])) → PROJ(top(band[Isla]) → yaxis) → READ(top(band[Isla]), y)≈6000..6900 ?wrong:read-cumulative-top-of-stack-not-band-thickness → ANSWER` | 16 | 0 | 15 | “you go from 2010 til you hit the top and then accross to find thw nuber” |
| `FIND(xtick[2010]) → FIND(band[Isla]) → READ(top(band[Isla]), y)≈6200..6500 ?wrong:read-cumulative-top-of-stack-not-band-thickness → ANSWER  (point on edge, no explicit projection)` | 4 | 0 | 4 | “Found the year on the x, and the line for Isla had the corresponding y value. I estimated in a range from 6300 to 6500 since I can't be precisely sure” |
| `FIND(band[Isla] \| legend/color) → FIND(xtick[2010]) → PROJ(→ top(band[Isla])) → PROJ(→ yaxis) → READ(y)≈6500 ?wrong:read-cumulative-top-of-stack-not-band-thickness → ANSWER` | 3 | 0 | 3 | “I identified the color that represents the name Isla, then identified the year 2010. Then traced the end point to the number of girls with that name” |
| `PROJ(xtick[2010] → top(band[Isla])) → INTERP(v \| ticks 6000,8000 or imagined grid) → READ(y)≈6500..6750 ?wrong:read-cumulative-top-of-stack-not-band-thickness → ANSWER` | 3 | 0 | 3 | “Just had to locate where the 'edge' of purple is in the year 2010. Getting an exact number is near to impossible, but I could make an estimate by guessing where 7000 is between 6000 and 8000 are..” |
| `READ(top(band[Olivia])@2010, y)≈12000 ?wrong:read-total-stack-height(top band) → ANSWER(≈12000)` | 3 | 0 | 3 | “I found this one colour blinding as the colours looked the same, correct answer is 6800” |
| `FIND(peak(band[Isla])) ?wrong:went-to-2012-peak-not-2010 → PROJ(→ yaxis) → READ(y)≈10500 → ANSWER(10500)` | 2 | 0 | 2 | “I made a mistake, I went for the peak of names and didn't focused on the year 2010, the correct answer would be around 6,500” |
| `READ(top(band[Amelia])@2010, y)≈4100..4200 ?wrong:wrong-band/read-Amelia-Isla-boundary → ANSWER` | 2 | 0 | 2 | “The drawing is correct however the amount that I entered was incorrect as I was looking at the wrong name and looked at the correct name on this question” |
| `KNOW(stacked: top = Isla+Amelia) → DOUBT → PROJ(→ top(band[Isla])) → READ(y)≈6500 ?wrong:read-cumulative-top-of-stack-not-band-thickness:knew-stacking-but-did-not-subtract → ANSWER(6500)` | 1 | 0 | 1 | “If I am reading the chart properly by adding Isla to Amelia's values then my drawing indicates my thought process.” |
| `MAP(top edge(band[Isla]) → value; band body is aesthetic) ?wrong → FIND(top(band[Isla])@2010) → PROJ(→ yaxis) → READ(y)≈6500 → ANSWER(6500)` | 1 | 0 | 1 | “I believe the top edge of the color is the value (the rest is just for esthetics/easier reading) so I found the point for 2010 and then read the number (estimated)” |
| `PROJ(top(band[Amelia]) → yaxis)≈4200 & PROJ(top(band[Isla]) → yaxis)≈6000 → READ(top(band[Isla]))≈6000 ?wrong:marked-both-boundaries-but-no-SEG → ANSWER(6000)` | 1 | 0 | 1 | “its on the 6000 mark” |

**Operations** (trials using it): `READ` 36, `PROJ` 33, `FIND` 32, `FIX` 4, `INTERP` 4, `MAP` 2, `COUNT` 1, `DOUBT` 1, `KNOW` 1, `CONFUSED` 1, `LOOK` 1, `CMP` 1

**Elements** (kind: text / sketch): `band` 6/36, `xtick` 12/27, `yaxis` 10/29, `color` 8/0, `ytick` 5/1, `legend` 3/2, `xaxis` 3/0, `grid` 3/0, `line` 2/0, `pt` 1/0, `chart` 1/0, `ytitle` 1/0, `question` 1/0, `mark` 1/0

**Specific elements:** `yaxis` 32, `top(band[Isla])` 31, `xtick[2010]` 31, `color` 7, `ytick[6000]` 4, `xaxis` 3, `grid` 3, `edge(band[Isla])` 3, `peak(band[Isla])` 3, `line[Isla]` 2, `ytick[8000]` 2, `top(band[Amelia])` 2

**New symbols:** `band[...] top/bottom`: top(band[X]) / bottom(band[X]) = upper/lower boundary of a stacked-area band (bottom(band[Isla]) = top(band[Amelia])); `ANSWER(v)`: the final reported response, used to show when a reported value departs from the read value; `line[Isla]`: participant's term for the band's boundary line (kept as written in the text)

## SAQ2 · stacked_area · make_comparison
> Over the course of years between 2009 and 2014, the number of girls named 'Isla' was always more than 'Amelia'. True or False?

n = 40 (correct 8), no process info: 0

**Reference:** `SCAN({xtick 2009..2014}) → for each x: SEG(top(band[Isla]) − top(band[Amelia])) vs READ(top(band[Amelia]), y) → e.g. @2012: SEG(10500 − 7000)≈3500 < 7000 → CMP(Isla < Amelia @2009..2013) → ANSWER(False)`

The pivotal confusion is between stack position and band thickness. Most participants traced the top edges of the purple and orange bands and concluded 'Isla is always above Amelia', which is True only by position. The 8 correct responders used thickness, through brackets or double arrows spanning each band at 2009/2012/2014 (P42, P56, P72), or through a holistic 'more orange area' judgement (P53, P65). Several participants knew the encoding was stacked ('Isla's numbers also include Amelia's', 'each colour represents the surplus') yet still compared tops. Two declared the chart unanswerable, and one read peak heights (~10500 vs ~7000) straight off the y-axis.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `TRACE(top(band[Isla])) → TRACE(top(band[Amelia])) → CMP(top(band[Isla]) > top(band[Amelia]) ∀ years) ?wrong:compared-stack-position/cumulative-top-not-band-thickness → ANSWER(True)  [often with MAP(color→name)]` | 14 | 0 | 13 | “the shaded section for Isla has always been above the shaded section for Amelia.” |
| `FIND(peak@2012) → PROJ(peak(band[Amelia]) → yaxis)≈7000 → PROJ(peak(top(band[Isla])) → yaxis)≈10500 → CMP(10500 > 7000) ?wrong:compared-stack-position/cumulative-top-not-band-thickness → ANSWER(True)` | 5 | 0 | 5 | “Isla had over 1000 named children at peak where amelia only had almost 7000” |
| `MAP(color → name) → CMP(band[Isla] above/higher than band[Amelia]) ?wrong:compared-stack-position/cumulative-top-not-band-thickness → ANSWER(True)  [position read from loops, labels, zigzags, no edge tracing]` | 4 | 0 | 4 | “colors were helpful, easy to compare since violet (Isla) is always above orange (Amelia)” |
| `SCAN({x}: arrow from top(band[Amelia]) or 0 up to top(band[Isla])) → CMP(Isla > Amelia per year) ?wrong:compared-stack-position/cumulative-top-not-band-thickness → ANSWER(True)` | 4 | 0 | 4 | “Every year there are more Islas than Amelias, i find the question confusing because if it is asking about the peak of Amelias compared to the peak of Islas, the itis false, but since i think is asking” |
| `READ(height(band[Amelia])) & READ(height(band[Isla])) at ≥1 year (brackets / double arrows) → CMP(height(band[Isla]) < height(band[Amelia])) → ANSWER(False)` | 3 | 3 | 0 | “The size of the color of "Isla" is instead smaller than the size of the color "Amelia"” |
| `SCAN(band[Isla]) → SCAN(band[Amelia]) → CMPvis(area(band[Amelia]) > area(band[Isla])) → ANSWER(False)` | 2 | 2 | 0 | “More area covered by Amelia names than Isla names.” |
| `TRACE(top edges) → CONFUSED(MAP(area size) vs MAP(position→yaxis)) → CMP(tops) ?wrong:compared-stack-position/cumulative-top-not-band-thickness → ANSWER(True)` | 2 | 0 | 2 | “Hard to identify whether to go with the size of the coloured area or the link to the numbers on the left” |
| `DOUBT/CONFUSED(chart cannot show exact amounts) → ANSWER(Impossible) ?wrong:declared-unanswerable` | 2 | 0 | 2 | “It hard to tell the exact amounts over the course of the year” |
| `KNOW(stacked: top(band[Isla]) includes Amelia) → TRACE(top(band[Isla])) → CMP(top above) ?wrong:compared-stack-position/cumulative-top-not-band-thickness:knew-cumulative-but-did-not-subtract → ANSWER(True)` | 1 | 0 | 1 | “I'm not familiar with reading these types of graphs but I assumed that because Isla's value is above Amelia, Isla's numbers also include Amelia's total.” |
| `GIST(chart) → ANSWER(False)` | 1 | 1 | 0 | “nothing was confusing, I just look and i know” |
| `FIND(legend) → PROJ(peak(band[Amelia])@2012 → yaxis)≈7000 → CMP(vs top(band[Isla])@2010) → ANSWER(False)  [right answer, unclear basis]` | 1 | 1 | 0 | “The simpleness of the graph was very helpful” |
| `TRACE(reference line through band[Isla]) → CMP(top(band[Amelia])@2012 > Isla line) → ANSWER(False)` | 1 | 1 | 0 | “There was nothing which was confusing, using the line you can see that at the end of 2011 beginning of 2012, there were more girls named Amelia than Isla” |

**Operations** (trials using it): `CMP` 32, `TRACE` 18, `FIND` 10, `MAP` 9, `SCAN` 9, `PROJ` 8, `LOOK` 6, `CONFUSED` 5, `READ` 5, `CMPvis` 3, `LABEL` 2, `GIST` 1, `TREND` 1, `KNOW` 1, `DOUBT` 1

**Elements** (kind: text / sketch): `band` 12/39, `xtick` 4/11, `color` 14/0, `yaxis` 1/5, `legend` 2/4, `line` 5/0, `chart` 3/1, `area` 4/0, `xaxis` 0/1, `mark` 1/0, `ytick` 1/0, `question` 1/0

**Specific elements:** `top(band[Isla])` 23, `top(band[Amelia])` 21, `band[Isla]` 17, `band[Amelia]` 12, `color` 9, `xtick[2012]` 7, `peak(band[Isla])` 7, `peak(band[Amelia])` 7, `yaxis` 6, `xtick[2009]` 6, `xtick[2014]` 6, `chart` 4

**New symbols:** `TRACE(e)`: follow a line/edge/boundary with the pen along its length (sketch evidence of attending to that contour over x); `LABEL(e 'text')`: participant writes a name/letter onto a mark to bind it to a series; `height(band[X])`: vertical thickness of a stacked band at a given x (bottom to top), as opposed to top(band[X]); `outline(band[X])`: the closed contour of a band (top and bottom edges)

## SAQ3 · stacked_area · find_extremum
> Over the course of years between 2009 and 2014, when was the number of girls named 'Isla' at the maximum?

n = 3 (correct 0), no process info: 0

**Reference:** `SCAN({xtick 2009..2014}: SEG(top(band[Isla]) − top(band[Amelia]))) ≈ {1900, 2400, 2900, 3500, 3500, 4700} → ARGMAX = 2014 → ANSWER(2014)`

All three participants used band thickness (height(band[Isla])), not the top-edge position. A top-edge reading would point to 2012, where the purple top peaks at ~10500. Two sketches are a single vertical span at 2014, and one participant wrote a relative thickness estimate inside the band at every year (1 to 2.4) and estimated about 4800 at 2014. All three answered 2014, which matches the key, yet the data records accuracy 0, so the accuracy field for this item looks mis-scored.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `READ(height(band[Isla])@2014, len) → ARGMAX(height(band[Isla])) = 2014 → ANSWER(2014)  [single vertical span at 2014]` | 2 | 0 | 2 | “That's the longest part, hence te time more girs were named Isla” |
| `SCAN({xtick}: READ(height(band[Isla])) written per year) → ARGMAX = 2014 → READ≈4800 → ANSWER(2014)` | 1 | 0 | 1 | “2014 highest with value of about 4800” |

**Operations** (trials using it): `ARGMAX` 3, `READ` 3, `FIND` 1, `SCAN` 1

**Elements** (kind: text / sketch): `band` 1/3, `xtick` 1/2, `chart` 1/0

**Specific elements:** `xtick[2014]` 3, `height(band[Isla])` 3, `band[Isla]` 2, `chart` 1

**New symbols:** `height(band[X])`: vertical thickness of a stacked band at an x position, read with channel len

## SAQ4 · stacked_area · characterize_trend
> The number of girls named 'Olivia' was __________ from 2009 to 2012.

n = 40 (correct 38), no process info: 0

**Reference:** `FIND(band[Olivia] \| legend[Olivia]→color[green]) → SCAN({xtick 2009..2012}: SEG(top(band[Olivia]) − top(band[Isla]))) ≈ {5200, 5300, 4900, 4600} → TREND(height(band[Olivia]), 2009..2012) = ↓ → ANSWER(Falling)`

The answer key is Falling, because the Olivia band gets thinner (~5200 to ~4600). The recorded accuracy field instead scores 'Rising' as 1 and the near-correct 'Constant' as 0, so the field looks inverted for this item, and n_correct_by_key is reported next to it. Almost everyone traced the rising top edge of the green band, which is the stack total, and read its slope as Olivia's trend. Only P85 and P108 compared band thickness at 2009 vs 2012: P85 called the change 'about the same', and P108 noticed afterwards that Olivia was 'actually falling'. Because Olivia is the top band, its top edge is the most salient element here, which is why the line-chart reading wins.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `[FIND(legend[Olivia])] → TRACE(top(band[Olivia]) 2009..2012) → TREND(top(band[Olivia])) = ↑ ?wrong:trend-of-cumulative-top-edge-not-band-thickness → ANSWER(Rising)` | 22 | 21 | 0 | “I just took the top line of the green for Olivia and saw that it gradually increased each year to 2012” |
| `PROJ(xtick[2012] → peak(top(band[Olivia]))) → PROJ(peak → yaxis)≈15000 [vs 2009 top ≈10700] → TREND = ↑ ?wrong:trend-of-cumulative-top-edge-not-band-thickness → ANSWER(Rising)` | 8 | 8 | 0 | “that a peak, the highest level.” |
| `TRACE(band[Olivia] interior / several band edges) → TREND = ↑ ?wrong:trend-of-cumulative-top-edge-not-band-thickness → ANSWER(Rising)` | 4 | 4 | 0 | “The slope of the curve kept rising” |
| `LOOK/loop(top(band[Olivia]) 2009..2012) → GIST(rising) ?wrong:trend-of-cumulative-top-edge-not-band-thickness → ANSWER(Rising)` | 2 | 2 | 0 | “I just look on the picture” |
| `TRACE(top(band[Amelia])) ?wrong:wrong-series → TREND = ↑ → ANSWER(Rising)` | 1 | 1 | 0 | “The orange part of the graphic increase between 2009 and 2012” |
| `READ(height(band[Olivia])@2009)≈5200 → READ(height(band[Olivia])@2012)≈4600 → CMP → TREND = → (judged ≈ constant) → ANSWER(Constant)` | 1 | 0 | 1 | “About the same amount” |
| `READ(height(band[Olivia])@2009, @2012) → CMP(<) → TREND = ↓ → FIX(Rising→Falling) [after entering Rising]` | 1 | 1 | 0 | “Error: Mistakenly looked at Amelia. Olivia names actually falling.” |
| `SCAN(height(band[Olivia]) strokes @2010..2012) → TREND = ↑ ?wrong:marked-thickness-but-judged-by-position → ANSWER(Rising)` | 1 | 1 | 0 | “I looked at the number of girls over the years” |

**Operations** (trials using it): `TREND` 39, `TRACE` 28, `PROJ` 14, `FIND` 13, `CMP` 5, `MAP` 5, `READ` 4, `LOOK` 3, `SLOPE` 2, `GIST` 1, `CONFUSED` 1, `FIX` 1, `SCAN` 1, `MAX` 1

**Elements** (kind: text / sketch): `band` 10/40, `xtick` 7/17, `color` 14/0, `yaxis` 2/8, `legend` 2/5, `line` 5/0, `xaxis` 2/1, `chart` 3/0, `trend` 2/0, `slope` 2/0, `area` 1/0, `question` 1/0

**Specific elements:** `top(band[Olivia])` 31, `xtick[2012]` 17, `xtick[2009]` 12, `peak(band[Olivia])` 11, `yaxis` 9, `color[green]` 7, `color` 6, `band[Olivia]` 6, `legend[Olivia]` 5, `line` 4, `chart` 3, `height(band[Olivia])` 3

**New symbols:** `TRACE(e)`: follow an edge/line with the pen along x; `height(band[X])`: vertical thickness of a stacked band at an x position; `bottom(band[X])`: lower boundary of a band (= top of the band beneath)

## SAQ5 · stacked_area · make_comparison
> In the UK, the number of girls named ‘Isla’ in 2014 was more than it was in 2013.

n = 40 (correct 5), no process info: 0

**Reference:** `FIND(band[Isla] \| legend[Isla]) → SEG(top(band[Isla])@2013 − top(band[Amelia])@2013) ≈ 9100−5600 = 3500 → SEG(top(band[Isla])@2014 − top(band[Amelia])@2014) ≈ 8100−3400 = 4700 → CMP(4700 > 3500) → ANSWER(True)`

Isla's band thickens from 2013 to 2014 (~3500 to ~4700), but its top edge falls (~9100 to ~8100) because Amelia shrinks underneath. That makes this item a near-perfect trap for top-edge reading. 35 of 40 answered False after comparing the Isla top edges, mostly with L-shaped projections to the y-axis or a downward trace. The correct responders measured band thickness, via brackets labelled 2.8/4.2 (P148), vertical spans with '<' (P136), or projecting all four boundaries (P139). Two 'True' answers contradict their own decline reasoning, and P138 noticed the purple band was bigger but explained it away as fewer Amelias.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `PROJ(xtick[2013] → top(band[Isla])) → PROJ(top@2013 → yaxis)≈9000 → PROJ(xtick[2014] → top(band[Isla])) → PROJ(top@2014 → yaxis)≈8000 → CMP(9000 > 8000) ?wrong:compared-cumulative-top-edge-not-band-thickness → ANSWER(False)  [L-shaped projections to y-axis at both years]` | 11 | 0 | 11 | “I identified the color that represented the name and measured the difference between the number of girls per year.” |
| `FIND/mark(top(band[Isla])@2013, @2014) → CMP(top@2013 > top@2014) ?wrong:compared-cumulative-top-edge-not-band-thickness → ANSWER(False)` | 10 | 0 | 9 | “As you can see on the graph the total number of girls with the name "Isla" went down.” |
| `TRACE(top(band[Isla]) 2013→2014) → TREND = ↓ ?wrong:compared-cumulative-top-edge-not-band-thickness → ANSWER(False)` | 8 | 0 | 8 | “the chart goes down indicating less” |
| `READ(height(band[Isla])@2013) & READ(height(band[Isla])@2014) → CMP(len@2014 > len@2013) → ANSWER(True)` | 3 | 3 | 0 | “Measure for Isla 2014 is 4200 and about 2800 for 2013.” |
| `LOOK(top(band[Isla])) → GIST ?wrong:compared-cumulative-top-edge-not-band-thickness → ANSWER(False)` | 2 | 0 | 2 | “I just look on the picture” |
| `FIND/TRACE(top(band[Olivia])) ?wrong:wrong-band(top-of-stack) → CMP/TREND ↓ → ANSWER(False)` | 2 | 0 | 2 | “I compared the points of 2013 and 2014 by which one is highest” |
| `TREND(top, 2012/2013..2014) = ↓ → ANSWER(True) ?wrong:answer-contradicts-own-reasoning` | 2 | 2 | 0 | “the turning point is in 2012 then from there it keeps decreasing.” |
| `FIND(peak(band[Isla])@2012) → PROJ(→ 2014) → CMP(lower) ?wrong:compared-cumulative-top-edge-not-band-thickness → ANSWER(False)` | 1 | 0 | 1 | “Clearly less popular” |
| `READ(height(band[Isla])@2013, @2014) → CONFUSED(all the purple) → ANSWER(False) ?wrong:marked-thickness-but-concluded-decrease` | 1 | 0 | 1 | “confusing to identify the overall number with such a large area to consider e.g. all the purple” |

**Operations** (trials using it): `CMP` 24, `PROJ` 22, `FIND` 15, `TREND` 12, `TRACE` 11, `LOOK` 4, `GIST` 3, `READ` 3, `CONFUSED` 2, `MAP` 2, `DIFF` 2, `CMPvis` 2, `KNOW` 1, `SEG` 1

**Elements** (kind: text / sketch): `band` 6/40, `xtick` 12/28, `yaxis` 1/13, `chart` 8/0, `legend` 3/4, `color` 6/0, `line` 2/0, `trend` 2/0, `xaxis` 1/0, `pt` 1/0, `trendline` 1/0, `grid` 1/0, `ytick` 1/0, `area` 1/0

**Specific elements:** `top(band[Isla])` 34, `xtick[2014]` 27, `xtick[2013]` 26, `yaxis` 14, `chart` 8, `band[Isla]` 7, `xtick` 4, `color` 4, `legend[Isla]` 4, `height(band[Isla])` 3, `legend` 3, `top(band[Olivia])` 3

**New symbols:** `TRACE(e)`: follow an edge/line with the pen along x; `height(band[X])`: vertical thickness of a stacked band at an x position

## SBQ1 · stacked_bar · retrieve_value
> What percentage of the room service cost in Copenhagen comes from the sandwich?

n = 20 (correct 0), no process info: 0

**Reference:** `FIND(seg[Copenhagen,Sandwich] \| legend[Sandwich]→color[blue], xtick[Copenhagen]) → PROJ(top(seg) → yaxis) → READ(y)≈24.3 → PROJ(top(bar[Copenhagen]) → yaxis) → READ(y)≈46.6 → PCT(24.3, 46.6)≈52 → ANSWER(52)`

No participant in this group got the item right. The dominant failure (11/20) is reading the dollar height of the Copenhagen sandwich segment (~24) off the $ y-axis and reporting it as the percentage, with no division by the bar total; a long horizontal line from the y-axis to the sandwich top is the signature sketch. The few who did read the total (~47) and form a ratio made arithmetic or estimation errors (45, 59, 60). The pivotal elements are the top of the whole Copenhagen bar (the denominator) and the sandwich-segment top; one participant even missed the title and said room service was not in the chart.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(seg[Copenhagen,Sandwich]) → PROJ(top → yaxis) → READ(y)≈24-25 ?wrong:read-$-value-as-percent → ANSWER` | 11 | 0 | 11 | “the blue colour represents sandwich and its almost at 25%” |
| `READ(top(bar[Copenhagen]),y) → READ(top(seg[Copenhagen,Sandwich]),y) → PCT(seg, total) ?wrong:arithmetic → ANSWER` | 3 | 0 | 3 | “the total cost is almost $50 and the price of a sandwich is almost 25 so the percentage must be around 45%” |
| `FIND(bar[Copenhagen]) → LOOK(seg[Copenhagen,Sandwich]) → ANSWER ?wrong:unexplained-overestimate` | 2 | 0 | 2 | “The blue represents the sandwich costs” |
| `LOOK(bar[Copenhagen]) → PCT(mid(bar))=50% → CMP(top(seg) vs mid) → PCT ?wrong:overestimate → ANSWER` | 1 | 0 | 1 | “calculated roughly where the 50% was and then calculated from there how much of that was just sandwiches” |
| `READ(top(bar[Copenhagen]),y)≈47 → PROJ(top(seg[Copenhagen,Sandwich]) → yaxis) → READ≈24 ?wrong:no-division → ANSWER` | 1 | 0 | 1 | “The total cost is around $47. From that, 24 percent (just below the 25 line) seems to be associated with Sandwich.” |
| `FIND(seg[Copenhagen,Water]) ?wrong:wrong-category → PCT → FIX → ANSWER` | 1 | 0 | 1 | “My mistake, I took 'water'.” |
| `FIND(question[room service] \| chart)=∅ ?wrong:missed-title → CONFUSED → ANSWER(0)` | 1 | 0 | 1 | “I couldnt, because room service is not mentioned in the graphic” |

**Operations** (trials using it): `READ` 16, `FIND` 13, `PROJ` 11, `LOOK` 5, `PCT` 5, `MAP` 5, `CMP` 4, `CONFUSED` 2, `DOUBT` 1, `FIX` 1

**Elements** (kind: text / sketch): `seg` 6/16, `yaxis` 2/11, `bar` 5/5, `color` 5/0, `ytick` 3/1, `legend` 4/0, `grid` 2/0, `chart` 2/0, `question` 2/0, `xtick` 1/0

**Specific elements:** `seg[Copenhagen,Sandwich]` 19, `yaxis` 11, `bar[Copenhagen]` 6, `color[blue]` 4, `legend[Sandwich]` 3, `ytick[25]` 3, `grid[y=25]` 2, `chart` 2, `mid(bar[Copenhagen])` 1, `question[room service]` 1, `legend[Water]` 1, `color` 1

**New symbols:** `mid(m)`: mark part: halfway point of a mark's extent (used as a 50% reference); `question[x]`: a specific phrase of the question text; `ANSWER(v)`: final reported answer (terminal step of a chain)

## SBQ2 · stacked_bar · find_extremum
> In which city is the cost of soda the highest?

n = 18 (correct 0), no process info: 0

**Reference:** `FIND({seg[*,Soda]} \| legend[Soda]→color[green]) → SCAN({seg[*,Soda]}) → CMPvis(len(seg[Stockholm,Soda]) > len(seg[Seoul,Soda]) > ...) → ARGMAX({seg[*,Soda]}, len)=Stockholm (≈53.3−43.8≈9.5) → ANSWER(Stockholm)`

Every answer in this group was wrong; 13/18 chose Helsinki because its soda segment sits highest on the y-axis (~63), i.e. they ranked the cumulative top position of the green segment rather than its length. Sketches show this clearly: circles on the Helsinki soda segment, lines from its top to the y-axis, or a horizontal line at ~63 across all bars. Two participants used the total Helsinki bar height (one by mistaking brown/Vodka for soda), and only one person compared segment lengths (Stockholm) but then picked the "impossible" option. The pivotal element is len(seg[*,Soda]), which requires SEG(top − bottom) on non-aligned baselines.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND({seg[*,Soda]} \| color[green]) → ARGMAX({seg[*,Soda]}, top-y)=Helsinki ?wrong:compared-cumulative-top-position-not-segment-length → (PROJ(top → yaxis)) → ANSWER(Helsinki)` | 13 | 0 | 13 | “Look for the tallest green bar because it represents soda.” |
| `FIND(bar[Helsinki]) → PROJ(top(bar[Helsinki]) → yaxis) ?wrong:used-total-bar-height → ANSWER(Helsinki)` | 2 | 0 | 2 | “Just measured the top of the brown square for Helsinki with the figures on the side” |
| `READ(top(bar[Helsinki]),y) → COUNT(grid) → READ(len(seg[Helsinki,Soda])) → ANSWER ?wrong:no-cross-city-comparison` | 1 | 0 | 1 | “I divide the numbers of horizontal lines between the height of the bar(total cost)” |
| `CMPvis(height(seg[*,Soda])) → ARGMAX(len)=Stockholm → ANSWER(Impossible) ?wrong:answer-mismatch` | 1 | 0 | 1 | “Stockholm seems to have the highest price as the green section seems to be biggest” |
| `SCAN({seg[*,Soda]}) → CONFUSED → ANSWER(not sure)` | 1 | 0 | 1 | “These charts are very confusing” |

**Operations** (trials using it): `FIND` 14, `PROJ` 9, `LOOK` 5, `ARGMAX` 5, `READ` 4, `MAP` 2, `CMP` 2, `CMPvis` 1, `CONFUSED` 1, `SCAN` 1, `COUNT` 1

**Elements** (kind: text / sketch): `seg` 10/16, `bar` 3/7, `color` 8/0, `yaxis` 2/4, `xtick` 1/3, `chart` 2/0, `legend` 1/1, `grid` 1/0, `ytick` 1/0

**Specific elements:** `seg[Helsinki,Soda]` 12, `yaxis` 6, `color` 5, `seg[*,Soda]` 5, `bar[Helsinki]` 5, `xtick[Helsinki]` 3, `bar[*]` 3, `top(bar[Helsinki])` 3, `top(seg[Helsinki,Soda])` 3, `color[green]` 2, `chart` 2, `seg[Stockholm,Soda]` 1

**New symbols:** `top-y (channel)`: ARGMAX/CMP keyed on the vertical position of a mark's top edge rather than its length

## SBQ3 · stacked_bar · make_comparison
> The cost of vodka in Helsinki is higher than that of Toronto.

n = 42 (correct 20), no process info: 0

**Reference:** `FIND(seg[Helsinki,Vodka] \| legend[Vodka]→color[orange], xtick[Helsinki]) → FIND(seg[Toronto,Vodka]) → SEG(68.6 − 63.1)≈5.5 → SEG(55.8 − 47.8)≈8 → CMP(5.5 < 8) → ANSWER(False)`

Accuracy split roughly in half (20/42 correct). The decisive split is the operand: people who compared the LENGTH of the two orange vodka segments (visually, with brackets/I-beams, or by projecting top and bottom edges to the axis and subtracting) answered False, while those who compared where the segments sit (top of the Helsinki bar at ~68.5 vs Toronto at ~56), often drawing a horizontal line across from Helsinki's top, answered True. A notable minority (5) explicitly could not decide whether the segment length or the cumulative height encodes vodka cost and chose Impossible/not sure. The non-adjacent bars and offset baselines make the length comparison hard, and one person marked the soda segments instead.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(seg[Helsinki,Vodka]), FIND(seg[Toronto,Vodka]) → PROJ(top(seg\|bar) → yaxis/across) → CMP(top-y Helsinki > Toronto) ?wrong:compared-cumulative-top-not-segment-length → ANSWER(True)` | 13 | 0 | 13 | “I drew a line acrross from Helsinki to toronto marking the highest price of Vodka” |
| `FIND(seg[Helsinki,Vodka]), FIND(seg[Toronto,Vodka]) → CMPvis(len/size(seg[Helsinki,Vodka]) < len/size(seg[Toronto,Vodka])) → ANSWER(False)` | 12 | 12 | 0 | “I visualized both orange boxes that represent the value of vodka and checked which one was bigger, regardless of it's starting position” |
| `PROJ(top/bottom(seg[Helsinki,Vodka]) → yaxis), PROJ(top/bottom(seg[Toronto,Vodka]) → yaxis) → SEG(top − bottom) / READ(len) ≈5 vs ≈8 → CMP → ANSWER(False)` | 8 | 8 | 0 | “Helsinki has about 5 unites when it comes to vodka where as Toronto has more than 5 units” |
| `FIND(seg[*,Vodka]) → CONFUSED(MAP(height(bar)→total) vs MAP(len(seg)→vodka)) → ANSWER(Impossible / not sure)` | 5 | 0 | 5 | “I am unsure if I had to look at the overall value (true) or just the vodka value (false).” |
| `FIND(seg[Helsinki,Vodka]), FIND(seg[Toronto,Vodka]) → CMPvis(len) ?wrong:misjudged → ANSWER(True)` | 2 | 0 | 2 | “I looked at the length of each section for vodka” |
| `FIND(seg[*,Soda]) ?wrong:wrong-category → CMPvis(len) → ANSWER(True)` | 1 | 0 | 1 | “the bar is bigger for Helsinki” |
| `FIND(bar[Helsinki]), FIND(bar[Toronto]) → ANSWER(True) ?wrong:unspecified` | 1 | 0 | 1 | “i looked at the bar graph of the said country” |

**Operations** (trials using it): `FIND` 31, `CMP` 18, `PROJ` 17, `CMPvis` 15, `CONFUSED` 6, `MAP` 6, `DOUBT` 4, `READ` 4, `SEG` 3, `LOOK` 2, `ARGMAX` 1

**Elements** (kind: text / sketch): `seg` 21/31, `bar` 11/8, `yaxis` 5/10, `color` 10/0, `legend` 3/3, `xtick` 3/2, `chart` 5/0, `grid` 1/1, `ytick` 0/1

**Specific elements:** `seg[Toronto,Vodka]` 24, `seg[Helsinki,Vodka]` 24, `yaxis` 12, `seg[*,Vodka]` 11, `bar[*]` 9, `top(bar[Helsinki])` 8, `top(seg[Helsinki,Vodka])` 8, `top(seg[Toronto,Vodka])` 8, `bottom(seg[Toronto,Vodka])` 7, `bottom(seg[Helsinki,Vodka])` 7, `color` 6, `bar[Helsinki]` 6

**New symbols:** `extent(m)`: the vertical span [bottom, top] of a mark, used when translating a segment to compare against another; `PROJ(e → right/across)`: projection drawn horizontally away from the y-axis or across to another bar rather than to the axis

## SBQ4 · stacked_bar · make_comparison
> The ratio of the cost of Soda to the cost of Water is higher in N.Y.C than in Stockholm. True or False?

n = 42 (correct 28), no process info: 0

**Reference:** `FIND(seg[N.Y.C.,Soda], seg[N.Y.C.,Water], seg[Stockholm,Soda], seg[Stockholm,Water] \| legend→color, xtick) → SEG(48.8−44.9)≈3.9, SEG(28.1−24.2)≈3.9 → RATIO≈1.0 (N.Y.C.) → SEG(53.3−43.8)≈9.5, SEG(32.5−28.4)≈4.1 → RATIO≈2.3 (Stockholm) → CMP(1.0 < 2.3) → ANSWER(False)`

Most participants (28/42) got this right, largely because the item is forgiving: N.Y.C. soda and water segments look about equal while Stockholm soda is obviously longer, so a quick per-city visual length comparison (or an explicit 1:1 vs ~2-3:1 estimate) suffices. Several people reasoned with differences instead of ratios; this happens to give the right answer for Stockholm, but it misleads when the "gap" is the vertical distance between segments (the intervening peanut band), which led to True. Others projected cumulative segment tops to the axis, compared only one of the two items, or gave up ("not sure") because of the four operands across two non-adjacent bars. The pivotal elements are the lengths of the four soda/water segments, not their positions.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(seg[Stockholm\|N.Y.C., Soda\|Water]) → CMPvis(len(soda) vs len(water) per city: N.Y.C. ≈, Stockholm >) → ANSWER(False)` | 11 | 11 | 0 | “For NYC, both water and soda seem the same size, while in Stockholm it is obvious that the price if soda is higher than water.” |
| `PROJ/SEG(len) ×4 → RATIO(soda,water \| N.Y.C.)≈1 → RATIO(soda,water \| Stockholm)≈2-3 → CMP → ANSWER(False)` | 9 | 9 | 0 | “Ratio for Soda to Water in NYC is 4:4 and 9:5 for Stockholm, Stockholm ratio higher.” |
| `FIND(4 segs) → CONFUSED / DOUBT → ANSWER(not sure / Impossible)` | 6 | 0 | 6 | “im not sure of this question as to where to watch or to look at” |
| `PROJ(top(seg) → yaxis) on cumulative positions ?wrong:cumulative-tops → (RATIO/CMP) → ANSWER` | 5 | 4 | 1 | “By comparing the figures on the side I found that the ratios were the same.” |
| `DIFF(soda, water) or vertical gap ?wrong:difference-not-ratio → CMP(N.Y.C. > Stockholm) → ANSWER(True)` | 4 | 0 | 4 | “there's a bigger gap between the cost of water and the cost of soda in NYC than in Stockholm” |
| `SEG(len) ×4 → DIFF(soda, water) ×2 ?wrong:difference-not-ratio(lucky) → CMP(Stockholm > N.Y.C.) → ANSWER(False)` | 3 | 3 | 0 | “Just compared each city and which had the greater difference, which was Stockholm.” |
| `compare only one item across cities (water only / soda only / crossed) ?wrong:partial-ratio → ANSWER` | 3 | 1 | 2 | “Stockholm sell more Soder than N.Y.C meaning its the one with a high ratio” |
| `PCT(soda, height(bar)) ×2 ?wrong:share-of-total → CMP → ANSWER(True)` | 1 | 0 | 1 | “Just seeing the percentage of the soda according to the height of the full spectrum” |

**Operations** (trials using it): `CMP` 22, `FIND` 21, `CMPvis` 12, `RATIO` 11, `PROJ` 11, `SEG` 8, `DIFF` 7, `DOUBT` 6, `CONFUSED` 5, `READ` 5, `LOOK` 5, `MAP` 4, `GUESS` 1, `PCT` 1, `FIX` 1

**Elements** (kind: text / sketch): `seg` 20/40, `yaxis` 4/8, `xtick` 6/2, `bar` 4/4, `color` 7/0, `chart` 4/0, `annot` 0/2, `question` 2/0, `legend` 1/1

**Specific elements:** `seg[N.Y.C.,Soda]` 26, `seg[N.Y.C.,Water]` 24, `seg[Stockholm,Soda]` 24, `seg[Stockholm,Water]` 23, `top(seg[Stockholm,Soda])` 9, `yaxis` 9, `top(seg[N.Y.C.,Soda])` 8, `seg[*,Water]` 7, `xtick[Stockholm]` 6, `color` 6, `top(seg[Stockholm,Water])` 6, `top(seg[N.Y.C.,Water])` 6

**New symbols:** `DIFF-as-ratio`: (pattern) a difference used as a stand-in for a ratio; coded as DIFF(...) ?wrong:difference-not-ratio

## SBQ5 · stacked_bar · retrieve_value
> What is the cost of peanuts in room service in Seoul?

n = 28 (correct 0), no process info: 0

**Reference:** `FIND(seg[Seoul,Peanut] \| legend[Peanut]→color[purple], xtick[Seoul]) → PROJ(top → yaxis) → READ(y)≈40.9 → PROJ(bottom → yaxis) → READ(y)≈34.8 → SEG(40.9 − 34.8)≈6.1 → ANSWER(6.1)`

No one in this group answered correctly (target 6.1). Half (14/28) projected the top of the purple Seoul segment to the y-axis and reported its cumulative position (~40-42), a horizontal line from the y-axis being the typical sketch. Others reported the bottom edge (35, read as a "minimum price"), the midpoint (37-40), or a range, and several said outright that they could not tell whether a segment's cost is its start, end, or length. The few who did subtract (top − bottom) snapped to the 35 and 40 ticks and got 5, or misread the 5-unit gridline step and got 11. The pivotal operation is SEG(top − bottom) on a floating segment, and nearly everyone skipped it.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(seg[Seoul,Peanut]) → PROJ(top → yaxis) → READ(y)≈40-42 ?wrong:read-cumulative-top-not-segment-length → ANSWER` | 14 | 0 | 14 | “Just drew thw line on the highest point of the peanut box” |
| `FIND(seg[Seoul,Peanut]) → PROJ(top & bottom → yaxis) → SEG(top − bottom)≈5 or 11 ?wrong:imprecise/scale-error → ANSWER` | 4 | 0 | 4 | “The purple bar on seoul - which indicates the peanuts- fits between 35-40 so the answer is 5” |
| `PROJ(bottom → yaxis)=35 (and top ≈41) → RANGE / MAP(bottom → min cost) ?wrong:position-not-length → ANSWER(35 or 40)` | 3 | 0 | 3 | “The minimum cost of peanuts in Seoul according to this chart is $35” |
| `READ(center(seg[Seoul,Peanut]) or AVG(position))≈37-40 ?wrong:midpoint-position → ANSWER` | 3 | 0 | 3 | “I did not know if I had to do the overall medium value (37) or take into account only the peanut value (5)” |
| `CONFUSED(encoding / room service) → ANSWER(0, 5, 49)` | 3 | 0 | 3 | “I am not sure if the cost start where the section for peanuts starts or ends.” |
| `READ(top(bar[Seoul]))=58 → READ(len(seg))≈7 → PCT ?wrong:percent-share → ANSWER(11)` | 1 | 0 | 1 | “Same problem as last time.” |

**Operations** (trials using it): `FIND` 21, `PROJ` 19, `READ` 17, `MAP` 5, `CONFUSED` 5, `SEG` 4, `DOUBT` 4, `LOOK` 4, `RANGE` 2, `FIX` 1, `PCT` 1, `AVG` 1

**Elements** (kind: text / sketch): `seg` 8/27, `yaxis` 3/18, `bar` 2/7, `color` 8/0, `chart` 6/0, `ytick` 4/0, `legend` 1/3, `xtick` 1/2, `annot` 0/1, `grid` 1/0, `question` 1/0

**Specific elements:** `yaxis` 19, `seg[Seoul,Peanut]` 16, `top(seg[Seoul,Peanut])` 15, `bar[Seoul]` 7, `chart` 6, `bottom(seg[Seoul,Peanut])` 6, `color` 5, `legend[Peanut]` 3, `ytick[35]` 3, `xtick[Seoul]` 2, `color[purple]` 2, `len(seg)` 1

**New symbols:** `MAP(bottom → minimum cost) / MAP(top → highest possible price)`: reading segment edges as a min/max price range instead of reading length as the value

## SB100Q1 · 100pct_stacked_bar · retrieve_value
> What percentage of Japan's Olympic medals are Bronze?

n = 8 (correct 0), no process info: 0

**Reference:** `FIND(seg[Japan,Bronze] \| legend[Bronze]→color[brown], xtick[Japan]) → PROJ(bottom(seg[Japan,Bronze]) → yaxis) → READ(y)≈71 → SEG(100 − 71)≈29 → ANSWER(≈29)`

No trial was correct. The dominant error was projecting the Japan bronze/silver boundary (~70) to the y-axis and reporting that cumulative position (69/71) instead of 100 − 71 ≈ 29. Others subtracted correctly but on the wrong bar (Australia, 48/49) or wrong segment (silver, 20), made an arithmetic slip (39), or split the bar into quarters (25). The pivotal step is SEG(top − bottom) on the correct segment.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(seg[Japan,Bronze]) → PROJ(bottom(seg[Japan,Bronze]) → yaxis) → READ(y)≈70 ?wrong:read-boundary-not-segment-length → ANSWER(≈70)` | 3 | 0 | 3 | “I think I was wrong by two numbers” |
| `FIND(seg[Australia,Bronze]) ?wrong:wrong-bar → PROJ(bottom → yaxis)≈52 → SEG(100 − 52) → ANSWER(48\|49)` | 2 | 0 | 2 | “it was abit tricky to calculate the percentage from top to bottom” |
| `FIND(bar[Japan]) → SPLIT(bar[Japan],4) → READ(seg[Japan,Bronze], len)≈1/4 ?wrong:coarse-estimate → ANSWER(25)` | 1 | 0 | 1 | “The blocks are helpful for estimations” |
| `FIND(seg[Japan,Bronze]) → PROJ(top → yaxis)=100 → PROJ(bottom → yaxis)≈71 → SEG(100 − 71) → ANSWER(39) ?wrong:subtraction-error` | 1 | 0 | 1 | “found the range then subtracted from 100” |
| `FIND(seg[Japan,Silver]) ?wrong:wrong-segment → PROJ(top,bottom → yaxis) → SEG(72 − 46) → ANSWER(20)` | 1 | 0 | 1 | “I estimated the percentage not sure if it is correct” |

**Operations** (trials using it): `FIND` 8, `PROJ` 6, `READ` 4, `SEG` 4, `DOUBT` 2, `SPLIT` 1

**Elements** (kind: text / sketch): `seg` 1/8, `yaxis` 0/5, `ytick` 2/0, `bar` 1/1, `xtick` 1/0, `grid` 0/1

**Specific elements:** `yaxis` 5, `bottom(seg[Japan,Bronze])` 4, `seg[Japan,Silver]` 2, `bottom(seg[Australia,Bronze])` 2, `bar[Japan]` 1, `seg[Japan,Gold]` 1, `seg[Japan,Bronze]` 1, `bar` 1, `xtick[Japan]` 1, `top(seg[Japan,Bronze])` 1, `seg[U.S.A.,Bronze]` 1, `grid[y=100]` 1

**New symbols:** `SPLIT(e, n)`: visually subdivides a mark into n equal parts to estimate a fraction

## SB100Q2 · 100pct_stacked_bar · make_comparison
> Who has the bigger percentage of Silver medals, Japan or Great Britain?

n = 3 (correct 0), no process info: 0

**Reference:** `FIND(seg[GB,Silver], seg[Japan,Silver] \| legend[Silver]) → PROJ(top,bottom of each → yaxis) → SEG(66−34)≈32, SEG(71−47)≈24 → CMP(32 > 24) → ANSWER(Great Britain)`

All three were wrong (Japan). One compared the top positions of the silver segments rather than their lengths, one compared the gold segments, and one stated that GB was larger but answered Japan. In this chart the floating silver segment's length, not its position, is pivotal.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(legend[Silver]) → FIND(seg[GB,Silver]), FIND(seg[Japan,Silver]) → CMP(top(seg[Japan,Silver]) > top(seg[GB,Silver])) ?wrong:compared-top-position-not-length → ANSWER(Japan)` | 1 | 0 | 1 | “Fist I focused on the silver medals then on the cities and then on which one was higher” |
| `FIND(seg[GB,Silver]) → FIND(seg[Japan,Silver]) → CMPvis(height(GB) > height(Japan)) → ANSWER(Japan) ?wrong:answer-contradicts-own-comparison` | 1 | 0 | 1 | “Great britain has more %than japan” |
| `FIND(seg[Japan,Gold]) ?wrong:wrong-category → FIND(seg[GB,Gold]) → CMPvis(height(GB,Gold) < height(Japan,Gold)) → ANSWER(Japan)` | 1 | 0 | 1 | “The part of the column representing the amount of golden medals earned by Japan is greater than that of Britain.” |

**Operations** (trials using it): `FIND` 3, `CMPvis` 2, `CMP` 1

**Elements** (kind: text / sketch): `seg` 1/3, `legend` 1/1, `xtick` 1/0

**Specific elements:** `seg[Great Britain,Gold]` 2, `seg[Japan,Gold]` 2, `xtick` 1, `legend[Silver]` 1, `top(seg[Japan,Silver])` 1, `seg[Japan,Silver]` 1, `seg[Great Britain,Silver]` 1

## SB100Q3 · 100pct_stacked_bar · find_extremum
> Which country has the highest number (absolute number, not %)  of Bronze medals?

n = 40 (correct 16), no process info: 0

**Reference:** `LOOK(ytitle[%]) → MAP(height(seg) → within-country share) → KNOW(share ≠ count without totals) → MISSING(total medals per country) → ANSWER(Impossible)`

This is a trick item. 16 of 40 were correct, mostly by noticing the "%" in the y-axis title or reasoning that totals per country are missing. The majority bracketed or circled the large Australia bronze segment and answered Australia, treating the within-country share as a count. Several drew horizontal lines from the Australia bronze bottom across all bars to compare. Some hedgers saw the problem but still answered Australia, and a few were "correct" only because they gave up.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `SCAN({seg[*,Bronze]}) → ARGMAX({seg[*,Bronze]}, len)=seg[Australia,Bronze] ?wrong:share-treated-as-count → ANSWER(Australia)` | 9 | 0 | 9 | “Australia has a the largest portion of bronze of total medals against other countries” |
| `SCAN({seg[*,Bronze]}) → PROJ(bottom(seg[Australia,Bronze]) → {bar[*]}\|yaxis) → ARGMAX(len)=Australia ?wrong:share-treated-as-count → ANSWER(Australia)` | 7 | 0 | 7 | “The biggest brown rectangle is for Australia, therefore I think is the one with the most bronze medals” |
| `[LOOK(seg[Australia,Bronze]) →] KNOW(segments are within-country shares; % ≠ count) → MISSING(totals) → ANSWER(Impossible)` | 5 | 5 | 0 | “Visualization refers to no absolute numbers just percentages (Australia having the largest percentage.” |
| `LOOK(ytitle[%]) → KNOW(only percentages shown) → MISSING(counts) → ANSWER(Impossible)` | 5 | 5 | 0 | “You can only see the percentage on this visualization.” |
| `LOOK(chart\|yaxis\|xtick) → MISSING(total medals per country) → ANSWER(Impossible)` | 4 | 4 | 0 | “perhaps I'm being stupid, but without any numbers, I can't work out the actual figures” |
| `FIND(seg[Australia,Bronze]) → ANSWER(Australia) ?wrong:share-treated-as-count` | 4 | 0 | 4 | “This one was simple, nothing complicated.” |
| `ARGMAX(len)=Australia → PROJ(top,bottom → yaxis) → DOUBT\|MISSING(totals) → ANSWER(Australia) ?wrong:share-treated-as-count` | 2 | 0 | 2 | “I think it is uncertain, because the chart does not give you number of medals, just %. But, considering that Australi...” |
| `LOOK(e) → CONFUSED(answer) → ANSWER(Impossible) [correct by default]` | 2 | 2 | 0 | “Couldn't find the answer” |
| `FIND(xtick[U.S.A.]) → LOOK(seg[U.S.A.,Bronze]) → ANSWER(U.S.A.) ?wrong` | 1 | 0 | 1 | “Looking for the USA in the bar graph” |
| `SCAN({bottom(seg[*,Bronze])}) → CONFUSED(term "absolute number") → ANSWER(not sure)` | 1 | 0 | 1 | “i dont undertand  what do you mean buy absolute number” |

**Operations** (trials using it): `ARGMAX` 19, `LOOK` 17, `SCAN` 14, `MISSING` 14, `PROJ` 11, `FIND` 10, `KNOW` 9, `MAP` 3, `CONFUSED` 3, `GUESS` 1, `DOUBT` 1, `CMP` 1, `SEG` 1

**Elements** (kind: text / sketch): `seg` 15/26, `annot` 13/0, `yaxis` 3/4, `bar` 3/4, `ytitle` 2/4, `color` 5/0, `xtick` 1/3, `grid` 0/4, `mark` 0/3, `xaxis` 1/1, `chart` 1/1, `label` 2/0, `ytick` 0/1, `legend` 0/1, `question` 1/0, `xtitle` 0/1

**Specific elements:** `seg[Australia,Bronze]` 20, `bottom(seg[Australia,Bronze])` 9, `yaxis` 7, `seg[*,Bronze]` 6, `annot[percentage]` 5, `annot[total medals]` 4, `ytitle[%]` 4, `grid[y=100]` 4, `color[brown]` 3, `seg[U.S.A.,Bronze]` 3, `bar` 3, `{bottom(seg[*,Bronze])}` 3

**New symbols:** `MISSING(x)`: participant judges required information (e.g. total medals per country) absent from the chart

## SPQ1 · scatter · retrieve_value
> What is the weight for the person who is 161 cm tall?

n = 1 (correct 0), no process info: 0

**Reference:** `FIND(xtick[161]) → PROJ(xtick[161] → pt[161cm]) → FIND(pt[161cm]) → PROJ(pt → yaxis) → INTERP(y \| ticks 40,45) → READ(pt, y)≈44.4 → ANSWER(≈44)`

Only one trial in this group. The participant used the right approach (find 161 on the x-axis, go up to the point, read its weight) but anchored on the 166 cm column, which is next to the sparse lower-left points, and read about 58 kg. They noticed the slip themselves afterwards. What matters on this item is the lone bottom-left point at (161, 44) and placing 161 between the 160 and 165 ticks.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(xtick[161]) ?wrong:picked-neighbouring-tick-166 → PROJ(xtick → pt) → READ(pt, y) → ANSWER` | 1 | 0 | 1 | “I looked for 161cm on the x-axis and then found the data point that fits. I'm only realizing now that I picked 166cm by mistake.” |

**Operations** (trials using it): `READ` 1, `PROJ` 1, `FIND` 1, `FIX` 1

**Elements** (kind: text / sketch): `xtick` 1/1, `pt` 1/1, `xaxis` 1/0

**Specific elements:** `xtick[161]` 1, `pt[161cm]` 1, `pt[166cm]` 1, `xaxis` 1, `xtick[166]` 1

## SPQ2 · scatter · find_extremum
> What is the height for the tallest person among the 85 individuals?'

n = 4 (correct 0), no process info: 0

**Reference:** `MAP(height → xaxis) → SCAN({pt[*]}) → ARGMAX({pt[*]}, x) = pt[182.4cm,63.5kg] → PROJ(pt → xaxis) → INTERP(x \| ticks 180,185) → READ(x)≈182.4 → ANSWER(≈182)`

All four trials are wrong, each for a different reason. One read 'tallest' as the highest point on the weight axis. One found the right point but misread the 5-unit tick spacing (185 instead of about 182). One gave the right height in metres (1.82). One picked the low-right outlier and gave its weight. The x-axis maximum (182.4 cm, 63.5 kg) and the nearly-as-tall outlier at (181.6, 45.8) compete as the 'tallest' point.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `ARGMAX({pt[*]}, y) ?wrong:'tallest'=highest-on-y → PROJ(pt → xaxis) → READ(pt, x) → ANSWER` | 1 | 0 | 1 | “Nothing was confusing” |
| `MAP(height → xaxis) → ARGMAX({pt[*]}, x) → PROJ(pt → xaxis) → INTERP(x \| ticks) ?wrong:misread-tick-increment → READ(x) → ANSWER` | 1 | 0 | 1 | “So here, it's just asking for the height so you can ignore the weight. I thought that the numbers indicated where on increments of 10s, s...” |
| `FIND(pt[rightmost]) → READ(pt, x) → ANSWER ?wrong:unit-converted-cm-to-m` | 1 | 0 | 1 | “everything was clear” |
| `FIND(pt[low-right, near-max x]) → PROJ(pt → yaxis) → READ(pt, y) ?wrong:reported-weight-not-height → ANSWER` | 1 | 0 | 1 | “look for the tallest person in the chart.” |

**Operations** (trials using it): `READ` 4, `FIND` 4, `PROJ` 3, `ARGMAX` 2, `FIX` 1, `MAP` 1, `INTERP` 1

**Elements** (kind: text / sketch): `pt` 1/4, `xaxis` 1/3, `yaxis` 0/2, `xtick` 1/0

**Specific elements:** `xaxis` 3, `pt[181.6cm,45.8kg]` 2, `yaxis` 2, `pt[176.8cm,74kg]` 1, `xtick` 1, `pt[182.4cm,63.5kg]` 1, `pt[tallest]` 1

## SPQ3 · scatter · determine_range
> What is the range in weight for the 85 individuals?

n = 13 (correct 0), no process info: 0

**Reference:** `MAP(weight → yaxis) → ARGMIN({pt[*]}, y)=pt[161cm,44.4kg] → ARGMAX({pt[*]}, y)=pt[176.8cm,74kg] → PROJ(both → yaxis) → READ(y)≈44.4, ≈74 → RANGE(44,74)`

The main split is between data extent and axis extent. Six of the 13 trials used extent-of-data (horizontal projections from the lowest and highest points to the weight axis, giving 44 to 74). Four circled or traced the axis end ticks (40 and 75). One switched to the height variable (161 to 182). The recorded accuracy is 0 for every scored trial, even those answering 44/74, which matches the stated correct range. This looks like a scoring artifact, so n_correct is low for that reason and not because of reasoning errors. The isolated extreme points (161,44) and (177,74) are the pivotal elements.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `ARGMIN({pt[*]}, y) → ARGMAX({pt[*]}, y) → PROJ(pt[min], pt[max] → yaxis) → READ(y)×2 → RANGE(min,max)` | 6 | 0 | 5 | “I found the highest and lowest weight by looking at the weight axis, these dots stood out to me also” |
| `READ(ytick[min]) → READ(ytick[max]) → RANGE(40,75) ?wrong:axis-extent-not-data-extent` | 4 | 0 | 4 | “Range refers to the measurement between two numbers. Therefore the range is between 40 to 75 kg” |
| `ARGMIN({pt[*]}, y) → ARGMAX({pt[*]}, y) → READ(pt, y)×2 → RANGE(min,max)  [extremes circled, no projection]` | 1 | 0 | 1 | “Looked at lowest and highest point” |
| `MAP(range → height) ?wrong:used-height-not-weight → ARGMIN/ARGMAX({pt[*]}, x) → PROJ(pts → xaxis) → READ(x)×2 → RANGE` | 1 | 0 | 1 | “The dots are visible and show the range in height clearly” |
| `SCAN(yaxis) → READ(ytick[75]) → ANSWER(75,-75) ?wrong:axis-extent+nonsense-bound → DOUBT` | 1 | 0 | 1 | “yes, i dont have the data for this question.” |

**Operations** (trials using it): `READ` 13, `RANGE` 12, `ARGMIN` 8, `ARGMAX` 8, `PROJ` 7, `LOOK` 3, `SCAN` 3, `OUTLIER` 2, `KNOW` 1, `MAP` 1, `DOUBT` 1

**Elements** (kind: text / sketch): `pt` 7/8, `yaxis` 3/9, `ytick` 1/4, `xaxis` 0/1, `chart` 1/0

**Specific elements:** `yaxis` 9, `pt[min-weight 44kg]` 7, `pt[max-weight 74kg]` 6, `pt[min-weight]` 5, `pt[max-weight]` 5, `ytick[40]` 4, `ytick[75]` 4, `chart` 1, `ytick[*]` 1, `pt[outlier]` 1, `pt[181.6cm,45.8kg]` 1, `pt[161cm,44kg]` 1

**New symbols:** `pt[max-weight 74kg] / pt[min-weight 44kg]`: a point identified by its role as the extreme on a channel (descriptive pt detail)

## SPQ4 · scatter · find_clusters
> There is a group of individuals centered at the height of 176 cm and the weight of 55 kg. True or False?

n = 39 (correct 33), no process info: 0

**Reference:** `FIND(xtick[176]) → FIND(ytick[55]) → PROJ(both → chart) → LOOK(region[176cm,55kg]) → COUNT({pt} in region)=0 → GROUP({pt[*]}) shows dense cluster near (170-174, 55-60) → CMP(cluster center ? (176,55)) → ANSWER(False)`

Most participants (34/39) answered False. The dominant gesture was a crosshair: a horizontal line from 55 kg and a vertical line from 176 cm meeting at an empty spot, sometimes circled. Variants were circling the empty region directly, projecting only vertically, or drawing outward arrows from a circled spot to both axes as a check. Errors came from reading 'centered at' loosely (accepting points along the 176 column or nearby as a group), from not knowing how many points make a group, and from stopping short when locating 176, which is not a labelled tick. Few participants located the real dense cluster (170-175 cm, 55-60 kg).

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(ytick[55]) → FIND(xtick[176]) → PROJ(both → chart) → LOOK(region[176,55]) → COUNT({pt} in region)=0 → ANSWER(False)  [crosshair]` | 16 | 15 | 0 | “There are no dots at 176 cm, therefore no one has that height while weighing 55 kgs.” |
| `FIND(xtick[176]) → PROJ(xtick → ytick[55]) → LOOK(region) → (COUNT=0) → ANSWER(False)  [vertical projection only]` | 6 | 6 | 0 | “I looked for the group of points around (176, 55) and there were none. The grid lines helps find the spot faster.” |
| `LOOK(region[176,55]) → COUNT({pt} in region)=0 → ANSWER(False)  [region circled directly]` | 5 | 5 | 0 | “I just noticed there were no dots in that area” |
| `LOOK(region[176,55]) → PROJ(region → yaxis) → PROJ(region → xaxis) → COUNT=0 → ANSWER(False)  [circle + outward arrows to axes as check]` | 4 | 4 | 0 | “I found the exact location where weren't any dots. The 176 was not on the scale, so it was hard to measure the right spot.” |
| `FIND(xtick[176]) → SCAN({pt: x≈176}) → CMP(center.y ? 55) → ANSWER(False)  [column-first]` | 2 | 2 | 0 | “I first had a glance of the one that were with 176 cm and then tried to find results with 55 kg” |
| `crosshair → COUNT({pt} near/along 176)>0 ?wrong:accepted-nearby-or-column-points → ANSWER(True)` | 2 | 0 | 2 | “Saw if there were many people at the given height and weight” |
| `crosshair or LOOK(region) → CONFUSED/DOUBT(what counts as a group) → ANSWER(Impossible / not sure) ?wrong` | 2 | 0 | 2 | “Not clear what number is considered a group” |
| `GROUP({pt[*]}) → cluster[170-175,55-60] → CMP(center ? (176,55)) → ANSWER(False)  [find actual cluster]` | 1 | 1 | 0 | “There is a group centred at around 55 to 60kg and 170 to 175 cm” |
| `FIND(xtick[176]) → PROJ(→ chart) ?wrong:stopped-short → CONFUSED(where to look) → ANSWER(not sure)` | 1 | 0 | 1 | “im not sure where to look for this one i am lost” |

**Operations** (trials using it): `LOOK` 35, `PROJ` 31, `FIND` 30, `COUNT` 23, `CMP` 6, `CONFUSED` 3, `SCAN` 2, `DOUBT` 1, `GROUP` 1, `INTERP` 1

**Elements** (kind: text / sketch): `region` 12/36, `xtick` 11/30, `ytick` 11/25, `pt` 14/3, `xaxis` 2/0, `cluster` 1/1, `grid` 2/0, `yaxis` 2/0, `chart` 1/0

**Specific elements:** `region[176cm,55kg]` 28, `ytick[55]` 27, `xtick[176]` 27, `pt` 11, `region` 9, `xtick[177]` 5, `region[177cm,55kg]` 4, `pt[176cm]` 3, `yaxis` 2, `xaxis` 2, `grid` 2, `xtick[174]` 1

**New symbols:** `region[x,y]`: an (often empty) location in the plot defined by an x,y coordinate pair or ranges, e.g. region[176cm,55kg]; `cluster[...]`: used as in spec, for a perceived dense group of points

## SPQ5 · scatter · find_correlation
> There is a negative linear relationship between the height and the weight of the 85 individuals. True or False?

n = 39 (correct 21), no process info: 0

**Reference:** `SCAN({pt[*]}) → FIT(trendline) → SLOPE(trendline) > 0 → CORR(height,weight)=+ → CMP(+ ? −) → ANSWER(False)`

Drawing a freehand upward trendline through the cloud was by far the most common strategy (19 trendlines), and nearly all of those answered False. Three drew the correct upward line but still answered True or 'not sure', so seeing the trend and mapping its sign to the claim are separate steps. Most failures were vocabulary confusion about 'negative linear' with no reading of the chart, or reasoning from a couple of extreme points (the tallest-but-light outlier, the lightest person) instead of the overall trend. Rare strategies: an upper/lower envelope, a staircase of sampled point projections, and a drawn negative-slope template compared against the cloud.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `SCAN({pt[*]}) → FIT(trendline) → SLOPE>0 → CORR=+ → ANSWER(False)  [drawn trendline]` | 15 | 14 | 0 | “There is a linear relationship but it is positive, as you can see from the line that I drew, as the height goes up the weight goes up” |
| `CONFUSED/DOUBT(question or 'negative linear') → ANSWER(not sure / Impossible)  [no reading of trend]` | 8 | 0 | 8 | “I'm not sure that we can be able to identify negative linear relationship in the chart.” |
| `SCAN({pt[*]}) → FIT(trendline) → SLOPE>0 → (fails to map sign to claim) ?wrong → ANSWER(True / not sure)` | 3 | 0 | 3 | “I can't answer this question, I don't understand it.” |
| `FIND(extreme pts) → PROJ(pts → axes) → CMP(extremes) → CORR from 2 points ?wrong:extreme-point-reasoning-not-trend → ANSWER(True / Impossible)` | 3 | 0 | 3 | “There is too many points which make it tricky to draw straight lines” |
| `GROUP({pt[*]}) → cluster[main] → CORR=0 or CONFUSED ?wrong → ANSWER(not sure)  [cloud enclosed]` | 2 | 0 | 2 | “There is no relationship” |
| `FIND(sampled pts) → PROJ(each → axes) → CMP(x↑ ⇒ y↑) → TREND=↑ → CORR=+ → ANSWER(False)  [point-pair staircase]` | 1 | 1 | 0 | “In general, it seems that the taller someone is, the heavier that person also is, so it is not a negative relationship” |
| `SCAN → FIT(trendline) + PROJ(sample pts → axes) → CMP(weight↑ ⇒ height↑) → CORR=+ → ANSWER(False)` | 1 | 1 | 0 | “The higher the weight the higher the height therefore it’s a positive relationship” |
| `GIST(chart) → FIT(upper & lower envelope ↗) → CORR=+ → ANSWER(False)  [envelope]` | 1 | 1 | 0 | “It was clear at first sight that is the opposite.” |
| `KNOW(negative shape) → DRAW(template[↘]) → CMP(cloud ? template) → FIX(→ False)  [template comparison]` | 1 | 0 | 1 | “After a bit more thinking, negative linear relationship should look like I drew I think, so I would change my answer to false.” |
| `GROUP({pt[*]}) → KNOW(height-weight related in real life) → ANSWER(False)` | 1 | 1 | 0 | “I dont understand clearly the answer, but I think is a coherent relation between the data according to the real life empirical relation w...” |
| `DOUBT('negative linear') → FIT(short local up-stroke) → ANSWER(False)` | 1 | 1 | 0 | “im not sure what negative linear relationship is exactly” |
| `SCAN → FIT(local polylines, mixed directions) → CORR=0 ?wrong:'random' → ANSWER(False)` | 1 | 1 | 0 | “the is no linear relationship between the height and weights all the values are random” |
| `FIND(ytick[85]) ?wrong:searched-axis-for-title-number → ANSWER(False)` | 1 | 1 | 0 | “There is no 85 in the chart.” |

**Operations** (trials using it): `CORR` 25, `FIT` 23, `SCAN` 23, `SLOPE` 18, `CONFUSED` 11, `CMP` 6, `FIND` 6, `KNOW` 5, `PROJ` 5, `TREND` 4, `GROUP` 4, `LOOK` 4, `GIST` 3, `DOUBT` 3, `AVG` 1, `RANGE` 1, `OUTLIER` 1, `DRAW` 1, `FIX` 1, `ARGMAX` 1, `ARGMIN` 1

**Elements** (kind: text / sketch): `trendline` 1/19, `pt` 8/9, `ytitle` 8/0, `xtitle` 8/0, `question` 7/0, `yaxis` 0/6, `line` 5/1, `xaxis` 0/3, `cluster` 0/3, `ytick` 0/3, `xtick` 0/2, `title` 1/0, `chart` 1/0, `template` 0/1, `envelope` 0/1

**Specific elements:** `trendline[↗]` 19, `ytitle` 8, `xtitle` 8, `question` 7, `yaxis` 6, `{pt[*]}` 5, `line` 5, `cluster[main]` 3, `pt[181.6cm,45.8kg]` 3, `xaxis` 3, `pt[161cm,44kg]` 3, `pt[outlier]` 2

**New symbols:** `FIT(trendline)`: draw or imagine a best-fit line through a point set (sketch: a freehand line through the cloud); `DRAW(template[...])`: draw a reference shape (e.g. what a negative slope would look like) to compare against the data; `trendline[↗]`: the participant-drawn trend line, with direction arrow; `envelope[upper|lower]`: a boundary line drawn along the upper or lower edge of a point cloud; `template[↘]`: a drawn hypothetical pattern, not fitted to the data

## SPQ6 · scatter · find_anomalies
> What is the height of the most prominent outlier in the data?

n = 9 (correct 0), no process info: 0

**Reference:** `SCAN({pt[*]}) → FIT(trendline ↗) → OUTLIER({pt[*]} \| distance from trend) = pt[181.6cm,45.8kg] → PROJ(pt → xaxis) → INTERP(x \| ticks 180,185) → READ(x)≈181.6 → ANSWER(≈182)`

Accuracy was not recorded for any trial. Only two participants (2/9) picked the true outlier, the tall-but-light point at (181.6 cm, 45.8 kg), and both then entered its weight (46) and corrected themselves in the text. Most people took 'most prominent outlier' to mean an extreme on one axis: the topmost point (176-177 cm, 74 kg) or the shortest and lightest point (161 cm, 44 kg). One chose the densest column. The pivotal element is spotting distance from the positive trend, which no one described explicitly.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `OUTLIER({pt[*]}) → pt[181.6,45.8] → READ(pt, y)≈46 ?wrong:reported-weight-not-height → ANSWER(46) → FIX(meant ≈182)` | 2 | 0 | 0 | “I confused the weight and height. The height is 181cm.” |
| `ARGMAX({pt[*]}, y) ?wrong:prominent=topmost → PROJ(pt → xaxis) → READ(x)≈176 → ANSWER(176)` | 2 | 0 | 0 | “I found the most prominent outlier and the I measured the height of it.” |
| `ARGMIN({pt[*]}, x & y) ?wrong:chose-shortest-lightest-point → PROJ(pt → axes) → READ(x)≈161 → ANSWER(161)` | 1 | 0 | 0 | “This person stands out the most, as they are the only individual with these stats. It is the shortest and lightest person.” |
| `SCAN → GROUP(several edge groups) → OUTLIER ?wrong:chose-lower-left-group → READ(x)≈161 → ANSWER(161)` | 1 | 0 | 0 | “more bigger bundle at the higher end” |
| `SCAN → GROUP(densest column) ?wrong:mode-not-outlier → READ(x)≈172 → ANSWER(172)` | 1 | 0 | 0 | “I saw where most of the dots were and went close to the actual number” |
| `CONFUSED → FIND(pt[topmost]) → PROJ(→ yaxis) → READ(y)≈74 ?wrong:weight-of-topmost → GUESS` | 1 | 0 | 0 | “am guessing, am confused.” |
| `DOUBT → LOOK(origin) → GUESS(150) ?wrong` | 1 | 0 | 0 | “i am not sure with this question” |

**Operations** (trials using it): `READ` 8, `OUTLIER` 5, `PROJ` 5, `FIND` 4, `SCAN` 2, `GROUP` 2, `FIX` 2, `GUESS` 2, `ARGMAX` 1, `LOOK` 1, `DOUBT` 1, `ARGMIN` 1, `INTERP` 1, `CONFUSED` 1

**Elements** (kind: text / sketch): `pt` 4/8, `yaxis` 0/5, `xaxis` 0/4, `ytitle` 2/0, `cluster` 1/1, `xtitle` 2/0, `xtick` 0/1

**Specific elements:** `xaxis` 4, `yaxis` 4, `pt[181.6cm,45.8kg]` 3, `pt[176.8cm,74kg]` 3, `pt[161cm,44kg]` 2, `ytitle` 2, `xtitle` 2, `cluster[higher end]` 1, `pt[182.4cm,63.5kg]` 1, `cluster[180-182cm,44-66kg]` 1, `cluster[162-163cm,46-48kg]` 1, `{pt: x≈172}` 1

**New symbols:** `GROUP(densest column)`: GROUP applied to pick the mode / densest vertical strip of points

## TMQ1 · treemap · find_extremum
> For which website was the number of unique visitors the largest in 2020?

n = 2 (correct 0), no process info: 0

**Reference:** `MAP(size(tile) → visitors) → SCAN({tile[*]}) → ARGMAX({tile[*]}, size)=tile[Google] → ANSWER(Google)`

Only two trials, both wrong: both participants declined to read area as value because the treemap has no key, legend or numeric scale. The sketches point at the root "Websites" header or write "No key", so the pivotal element is the absent size legend, not any tile.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `LOOK(chart) → MISSING(legend\|value key) → ANSWER(Impossible) ?wrong:area-encoding-is-conventional` | 2 | 0 | 2 | “It doesn't state that the bigger the box the higher the number of visitors” |

**Operations** (trials using it): `MISSING` 2, `LOOK` 2, `DOUBT` 1, `MAP` 1

**Elements** (kind: text / sketch): `annot` 1/1, `tile` 1/1, `legend` 1/0

**Specific elements:** `size(tile)` 1, `tile` 1, `annot[Websites]` 1, `tile[Google]` 1, `annot[scale]` 1, `legend` 1

**New symbols:** `MISSING(x)`: participant judges that information needed to answer (key, scale, values, totals) is absent from the chart

## TMQ2 · treemap · make_comparison
> The number of unique visitors for Amazon was more than that of Yahoo in 2020. True or False?

n = 41 (correct 29), no process info: 0

**Reference:** `MAP(size(tile) → visitors) → FIND(tile[Yahoo!]) → FIND(tile[Amazon]) → CMPvis(size(tile[Yahoo!]) > size(tile[Amazon])) → ANSWER(False)`

Most participants outlined, circled or scribbled over the Yahoo! and Amazon tiles and judged area directly; a few measured width and height with arrows or estimated a ~2:1 ratio. Errors came from comparing Google instead of Amazon (2), from refusing to read area without numbers or a key (several "Impossible" or "not sure"), from one within-group share comparison (Amazon large relative to Retail), and from one participant whose overlay showed Amazon at half of Yahoo! but who still answered True.

**Strategies people used**

| chain | n | ✓ | ✗ | example |
|---|---|---|---|---|
| `FIND(tile[Yahoo!]) → FIND(tile[Amazon]) → CMPvis(size(tile[Yahoo!]) > size(tile[Amazon])) → ANSWER(False)` | 21 | 21 | 0 | “Was trying to make a spot the difference drawing to make my answer clear and the drawing helped.” |
| `FIND(tile\|label[Yahoo!], tile\|label[Amazon]) → CONFUSED(MAP(size\|shape\|color → visitors)) → ANSWER(Impossible) ?wrong:did-not-map-area-to-value` | 4 | 0 | 4 | “I am not sure if the number of visitors has to do with the size, shape or colour.” |
| `[FIND(tile[Yahoo!]) → FIND(tile[Amazon]) →] MISSING(values\|scale) → ANSWER(Impossible\|not sure) ?wrong:area-encoding-is-conventional` | 4 | 0 | 4 | “Still no actual numbers to come to that conclusion reliably.” |
| `FIND(tile[Google]) ?wrong:compared-Google-instead-of-Amazon → FIND(tile[Yahoo!]) → CMPvis(size(tile[Google]) > size(tile[Yahoo!])) → ANSWER(True)` | 2 | 0 | 2 | “googles area is much bigger than yahoo” |
| `FIND(tile[Yahoo!]) → FIND(tile[Amazon]) → LOOK(width,height of each) → CMPvis(size(tile[Yahoo!]) > size(tile[Amazon])) → ANSWER(False)` | 2 | 2 | 0 | “The surface area of the different categories in clearly not equal” |
| `FIND(tile[Yahoo!]) → FIND(tile[Amazon]) → CMP(visitors(Yahoo!) > visitors(Amazon)) → ANSWER(False)` | 2 | 2 | 0 | “The number of unique visitors for Yahoo was more than that of Amazon in 2020.” |
| `FIND(tile[Yahoo!]) [→ FIND(tile[Amazon])] → ANSWER(False)` | 2 | 2 | 0 | “there is no numbers to answer this question” |
| `FIND(tile[Yahoo!]) → FIND(tile[Amazon]) → LOOK(width/height) → RATIO(size(tile[Yahoo!]), size(tile[Amazon]))≈2 → ANSWER(False)` | 2 | 2 | 0 | “I compared their sizes. Amazon is more or less half of Yahoo! size, therefore it is false.” |
| `FIND(tile[Amazon]) → FIND(tile[Yahoo!]) → OVERLAY(tile[Amazon] → tile[Yahoo!]) → RATIO≈0.5 → ANSWER(True) ?wrong:answer-contradicts-own-comparison` | 1 | 0 | 1 | “The rectangle of amazon seems to be about half of the size of Yahoo! rectangle.” |
| `FIND(tile[Yahoo!]) → FIND(tile[Amazon]) → CMP(share of group[Retail] vs share of group[Search/Portal]) ?wrong:within-group-share → DOUBT → ANSWER(not sure)` | 1 | 0 | 1 | “I don't really know but i think yes because the shape for amazon is bigger compared to other retailers than yahoo's c...” |

**Operations** (trials using it): `FIND` 39, `CMPvis` 25, `LOOK` 7, `MISSING` 5, `RATIO` 4, `CONFUSED` 4, `MAP` 4, `CMP` 3, `OVERLAY` 1, `DOUBT` 1

**Elements** (kind: text / sketch): `tile` 33/37, `label` 4/4, `annot` 1/1, `group` 1/1, `chart` 1/0, `color` 1/0

**Specific elements:** `tile[Yahoo!]` 35, `tile[Amazon]` 31, `size(tile)` 8, `height(tile[Yahoo!])` 4, `label[Yahoo!]` 4, `label[Amazon]` 4, `width(tile[Yahoo!])` 3, `width(tile[Amazon])` 3, `tile` 3, `label[values]` 3, `size(tile[Yahoo!])` 2, `tile[Google]` 2

**New symbols:** `MISSING(x)`: participant judges required information (values, scale, key) to be absent from the chart; `OVERLAY(a → b)`: redraws/transposes the outline of mark a onto mark b to compare sizes directly; `group[name]`: a treemap parent category rectangle (e.g. group[Retail]) containing child tiles; `shape(m)`: the shape of a mark as a possible encoding channel
