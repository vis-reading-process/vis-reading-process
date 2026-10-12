# Step-trace codebook (pilot re-code of Nobre et al. 2024 explanations)

Goal: convert each participant's free-text explanation (and, when provided, their sketch) into an
ordered **trace of typed steps**, coding ONLY what the evidence supports. Do not fill in steps the
participant "must have" done. A missing step is data (it tells us the elicitation didn't capture it).

## Inputs per trial
- chart image (path), question text, participant answer (+ accuracy: 1 correct / 0 incorrect / blank unknown)
- explanation text (verbatim)
- sketch image (only in the sketch condition): the participant's mouse drawing over the chart, showing where they found the answer

## Step types
| type | meaning | args (fill what's evidenced; else null) |
|---|---|---|
| PLAN | statement of how they interpreted the task / what they set out to find | `target` (what they looked for), `op` (intended operation, e.g. "range=first..last") |
| ATTEND | looked at / used a chart *component* | `component` ∈ {title, x_axis, y_axis, axis_labels, legend, colormap, gridline, annotation, mark, mark_group, whole_chart} ; `detail` (e.g. "green bars", "Tokyo bubble") |
| ENCODE | stated (or clearly implied) belief about what a visual channel means | `channel` ∈ {position_x, position_y, length, height_segment, area, size, color, angle, slope}, `maps_to` (what they think it represents) |
| EXTRACT | read a specific value or ordinal relation off the chart | `element` (which mark/category/time), `channel`, `value` (number/label if stated, else null) |
| COMPUTE | operation on extracted values (incl. visual estimation of a derived quantity, comparison, ordering) | `op` ∈ {compare, difference, sum, ratio, average, max_min, count, trend, estimate_derived, sort, other}, `inputs`, `result` |
| KNOW | used knowledge not in the chart (term definition, world knowledge, plausibility check, causal explanation, expectation) | `claim`, `role` ∈ {define_term, sanity_check, fill_gap, override, explain} |
| MONITOR | metacognitive: doubt, confusion, checking, self-correction | `kind` ∈ {confusion, uncertainty, check, self_correction}, `about` |
| ANSWER | explicit statement of the final answer in the explanation | `value` |

Order steps as the participant narrates them; if no order cue exists, keep text order and set `order_evidenced=false`.

## Error tags (attach to a step, only for the step where the error is evidenced)
Reuse Nobre et al. barriers, now step-level:
- on PLAN: `T1_task_concept` (wrong concept, e.g. range=endpoints), `T2_wrong_target` (wrong category/year), `T3_confused_by_question`
- on ENCODE / ATTEND: `E1_encoding` (wrong channel meaning, e.g. stacked segment top = value), `E2_axis_colormap`, `E3_layout_as_data` (axis extent/chart centre treated as data)
- on EXTRACT: `D1_wrong_element`, `D2_wrong_channel`, `D3_wrong_value` (incl. estimation, unit, decimal)
- on COMPUTE: `C_arith` (calculation slip), `C_wrong_op` (wrong aggregation), `E4_cannot_estimate`
- on KNOW: `K_override` (prior beats data), `K_causal_leap`, `K_wrong_definition`

## Per-trial summary fields
- `n_steps` (excluding MONITOR-only filler like "nothing was confusing")
- `stages_present`: subset of {A, E, C, K} where A=ATTEND or ENCODE, E=EXTRACT, C=COMPUTE, K=KNOW
- `order_evidenced`: true if text gives sequence cues ("first", "then", "after", clear chained steps)
- `reconstructable`: 0 = no process info (e.g. "it was easy", "I guessed"), 1 = partial (one step or vague), 2 = enough to replay the path to the answer
- `first_error_step`: index of first step carrying an error tag, or null
- `error_localizable`: true if the evidence pinpoints at which step the participant went wrong (only meaningful for incorrect trials)
- `notes`: ≤ 20 words, only if something is unusual
- sketch condition only: `sketch_adds`: list of what the sketch contributed beyond text, from {element_identified, value_location, channel_identified, path_order_hint, contradicts_text, nothing, unreadable}

## Calibration examples
1. "I found the values for the two months, then ordered them from first to last." (ACQ3, wrong)
   → PLAN(op="range=endpoints", err T1) · EXTRACT(Jan 2018) · EXTRACT(Jan 2020) · COMPUTE(sort); stages {E,C}; order_evidenced=true; reconstructable=2; first_error_step=0; localizable=true
2. "Look for the tallest green bar because it represents soda." (SBQ2)
   → ENCODE(color→soda) · ATTEND(mark_group "green bars") · COMPUTE(max_min); stages {A,C}; reconstructable=2
3. "It was easy, nothing confusing." → steps []; reconstructable=0
4. "Peanuts cost between 35 and 42 dollars. So the average cost is 38." (SBQ5, wrong)
   → ENCODE(height_segment → "price range", err E1) · EXTRACT(Seoul peanuts bottom=35) · EXTRACT(top=42) · COMPUTE(average→38); stages {A,E,C}; reconstructable=2; first_error_step=0
5. "The x-axis are confusing!" → ATTEND(x_axis) · MONITOR(confusion, x_axis); reconstructable=1
