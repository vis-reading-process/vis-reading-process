# Process-level visualization literacy: audit of prior data + study scaffolding

Target process stages (any order, recurring):
**(A) Attend** to vis components · **(E) Extract** values · **(C) Compute** on values · **(K) Integrate prior Knowledge**

---

## 1. Does the linked prior work produce process-level data?

### Nobre et al. 2024, *Reading Between the Pixels* (CHI '24) + supplementary

**What they collected** (verified in `supplementary 2/`):

| Signal | Detail | Process-level? |
|---|---|---|
| Open numeric answer + "not sure"/"impossible" | 1,774 trials, 120 Prolific participants, 4 of 12 VLAT charts each | Outcome only, but open numbers carry *some* path info (a wrong value often points to the step that went wrong) |
| Free-text rationale ("Can you explain your thought process? What elements guided your decision? Did you find any part confusing?") | 817 non-empty explanations; **489 on incorrect trials, 312 on correct**; **median 11 words, 48% ≤ 10 words** | Thin. Retrospective, uncued, mostly a single clause ("I used the colour to pick the right section") |
| Sketch on chart (Qualtrics signature widget) | Final PNG per incorrect trial (`annotations/`, `composite_annotations/`) | Spatial evidence of *what* was attended/extracted, but **no stroke order or timing**, so no sequence |
| Timing | First click / last click / submit per page | Total latency only |
| Codes (MAXQDA → `00_Barriers.csv`, `codes.csv`) | Per-trial **error** codes: T1–T3, E1–E4, D1–D3 (+ subcodes), "Realized mistake when drawing", "correct logic" | Codes say *what went wrong*. The full chain of steps is not coded |

**Verdict: not process-level, though it gets close.** The paper describes a staged process (pose question → translate → encode/layout → decode → synthesize), and Fig. 4–7 draw "pathways" such as T1 → D1 → ✗. Those pathways were **inferred by the coders**. They were not observed. Specific gaps:

1. **Selection bias.** Rationale was elicited only after a wrong answer or "not sure", so there are no traces of successful strategies. The authors list this as future work.
2. **No sequence.** Neither the text nor the sketches record order, so recurring loops (e.g., legend → mark → legend) can't be recovered.
3. **Stage coverage is uneven.** Using a crude keyword pass over the 817 explanations: ~20% mention a component (axis/legend/colour…), ~34% an extraction, ~14% a computation, ~5% prior knowledge. Prior knowledge (K) is essentially absent because VLAT items are designed to be answerable from the chart alone. The authors explicitly put stages 1 and 5 out of scope.
4. **Computation is folded into encoding.** E4 ("cannot visually estimate a derived value") is the only compute-like code. A wrong subtraction is not separated from a wrong read.
5. **Reactivity.** 39 trials (8% of errors) were coded "realized mistake when drawing". Elicitation changes the process. That's useful as a pedagogy finding, but it confounds measurement.

**Still very reusable:**
- The T/E/D taxonomy maps cleanly onto *step-level error labels* in a trace grammar (see §2).
- The 817 explanations + sketches make a ready pilot corpus for testing whether a step grammar can be applied reliably.
- The design-variant manipulations (histogram label A/B, area-chart dataset A/B) show how to build items whose wrong answers diagnose a path.

### McNutt, Kindlmann & Correll 2020, *Surfacing Visualization Mirages* (CHI '20)

This is a conceptual pipeline model (Curating → Wrangling → Visualizing → **Reading**) with a taxonomy of failure modes. It has no participant data and is **not process-level data**. Its *Reading* stage is still the most useful source for stage **K**: assumption of causality, base-rate neglect, anchoring on initial framing, confirmation bias, assuming data is complete. These are concrete ways prior knowledge *enters* the reading process, and they can serve as sub-labels for K steps.

### Your NYT "What's Going On In This Graph?" pipeline (`vis-inference-modeling`)

Open notice/wonder comments are decomposed into ACE sentences and tagged visual vs. non-visual. This is rich on **K** and on inference, but there is no task and no ground truth. It is also a product-level description, not an ordered process. The clause-segmentation + LLM-tagging machinery transfers directly to coding think-aloud transcripts (§4).

---

## 2. Breaking process-level data down: a trace grammar

Represent each trial as an **ordered trace of typed steps** that form a DAG through value references. This allows any order, repetition, and backtracking.

```
PLAN     (task_interp, target, qualifiers)          # Nobre "translation"
ATTEND   (component)                                 # title | axis-x | axis-y | legend | colormap | mark[id] | gridline | annotation | question-term
ENCODE   (belief: channel -> data field)             # explicit encoding model, e.g. "segment height = absolute value"
EXTRACT  (element, channel, value, unit) -> v_i      # e.g. EXTRACT(bar[JP,Bronze], length, 20, %) -> v1
COMPUTE  (op, inputs[v_i..], result) -> v_j          # op: diff|sum|ratio|mean|compare|argmax|count|trend|estimate
KNOW     (claim, role)                               # role: define-term | sanity-check | fill-gap | override | explain/causal
MONITOR  (check, outcome)                            # re-read, doubt, self-correction ("realized when drawing")
ANSWER   (value, confidence)
```

Each step can carry an **error tag** that reuses Nobre's taxonomy, which now attaches to a *step* rather than a *trial*:

| Nobre barrier | Lives on step | Tag |
|---|---|---|
| T1 misunderstands task / T2 misreads target | PLAN | wrong op / wrong target |
| E1 wrong encoding / E2 axis-colormap / E3 layout-as-data | ENCODE (or ATTEND to wrong component) | wrong mapping belief |
| D1 wrong element / D2 wrong channel / D3 wrong value | EXTRACT | element / channel / magnitude error |
| E4 can't estimate derived value | COMPUTE | missing/approximate op |
| *(new)* arithmetic slip, wrong aggregation | COMPUTE | op/arith error |
| *(new)* prior overrides data, causal leap, base-rate | KNOW | McNutt "Reading" mirages |

**Reference traces.** For each item, write one or more expert solution traces. Align each participant trace to them. The **first divergent step** localizes the barrier, and later errors are cascades. Nobre describe cascades in prose, and this alignment turns them into data. It also gives a natural modelling target: P(next step | chart, task, history), or an HMM / process-mining model over step types.

Example: Nobre ACQ3 ("range of coffee prices Jan 2018–Jan 2020"):
```
ref : PLAN(range=min..max over interval) → ATTEND(x-axis) → EXTRACT(min mark)→v1 → EXTRACT(max mark)→v2 → ANSWER(v1–v2)
obs : PLAN(range=endpoints)[T1] → ATTEND(x-axis) → EXTRACT(Jan18)→.73 → EXTRACT(Jan20)→.89 → COMPUTE(sort) → ANSWER(.73–.89)
```

---

## 3. Experiment / trial scaffolding

The core tension is that **more structure gives cleaner traces but more reactivity**: forcing people to verbalize can change what they do. The design therefore uses (a) layered signals that range from non-reactive to explicit, and (b) conditions that *measure* the reactivity cost.

### 3.1 Trial flow (per item)

```
┌ 1. Question alone (3–5 s, no chart)          → captures PLAN separately from reading
│    optional probe (cond. B only): "What will you need to find?"  [short text / select]
├ 2. Chart + question, instrumented            → passive ATTEND/EXTRACT signals
│    • restricted-focus reveal (blurred chart; hover/click a region to un-blur, BubbleView-style)
│      or cursor tracking / webcam gaze (WebGazer) / lab eye-tracking with AOIs per component
├ 3. Answer: open numeric/text + confidence (0–100)
├ 4. Step reconstruction (structured "step builder", see 3.2)
│    cued by a replay of their own reveal/hover timeline
├ 5. Knowledge probe: "Did you use anything you knew beyond the chart?" (Y/N + text)
│    + "Does this result surprise you?" (prior-consistency)
└ 6. (subset) Decomposed sub-probes on the SAME item, AFTER answering:
     "What does segment height represent?" → ENCODE
     "What is the value of Japan-Bronze?" → EXTRACT
     "Given 20 and 49, what is X?"        → COMPUTE
     Correct parts with a wrong composite localize the failure without relying on verbal report.
```

Elicit steps 4–5 on **all trials** (or a random 50%), not only on errors. This fixes Nobre's selection bias.

### 3.2 The step builder (structured but not leading)

The answer is built as a chain of cards. Each card is one of four verbs, matching your four stages, plus "just saw it":

| Card | Input widget | Auto-logged |
|---|---|---|
| **Look at…** | click a chart region (snaps to component AOI: axis, legend, mark) | component id, order |
| **Read a value** | click the mark + type value + unit | element, channel (inferred from AOI), value |
| **Calculate** | built-in calculator that references earlier values (v1 − v2) | op, operands, result |
| **Used what I know** | free text + role dropdown (define a term / sanity-check / fill a gap / explain why) | K step |
| **Just saw it** | none | marks perceptual or gist steps, so automatic processes aren't forced into fake sequences |

Cards can be reordered and repeated, which preserves recurring order. The final card's output is checked against the step-3 answer, and any mismatch is itself informative.

### 3.3 Between-subjects conditions (to quantify reactivity)

| Cond | During trial | After trial | Purpose |
|---|---|---|---|
| **0 Control** | plain chart | answer only | baseline accuracy/RT |
| **A Passive** | restricted-focus / cursor log | answer | non-reactive A/E signal |
| **B Retrospective-structured** | passive log | step builder (cued replay) | main scalable dataset |
| **C Concurrent-structured** | step builder *is* the answer UI | — | max structure; reactivity estimate (vs 0) |
| **D Think-aloud** (n≈20–30, lab or Prolific audio, ± eye-tracking) | concurrent verbalization (Ericsson & Simon level 1–2, no "why") | cued retrospective | gold standard to validate B/C traces |

Key analyses: accuracy/RT shift in C and B vs 0 (reactivity), and agreement between B traces and D-coded traces (validity of the scalable method).

### 3.4 Item design so the process becomes identifiable

- **Path-diagnostic numeric items.** Choose data so each plausible strategy gives a *distinct* answer: endpoints vs. min/max (range), segment vs. cumulative height (stacked), degrees vs. % (pie), y vs. x (scatter). The answer alone then votes for a path, which gives a cheap process signal at scale. Nobre's area-chart A/B shows the idea.
- **Graded compute load.** Use 0 ops (retrieve) → 1 op (compare/diff) → 2+ ops (ratio, aggregate over k marks) on the same chart, so C can be separated from E.
- **Graded attention load.** Direct labels vs. legend, legend position, number of series. This changes how many ATTEND steps a correct path needs.
- **Prior-knowledge manipulation (stage K).** Use the same chart structure with labels that are (i) real and congruent with common beliefs, (ii) real but counter-intuitive, (iii) neutral ("Product A"), (iv) counterfactual. Optionally elicit the prior *before* the chart (belief-elicitation paradigm). Drift of answers toward the prior, plus KNOW cards and gaze on title/labels, gives a measurable K. VLAT alone cannot do this.
- **Q-matrix.** Tag every item with the steps its reference trace requires (A, E, C, K, ENCODE type). This enables cognitive-diagnostic models (DINA/G-DINA) on the answer data, which can then be checked against the traces.
- Keep Nobre's ambiguity fixes (histogram labels, explicit year boundaries) unless ambiguity is the manipulation.

### 3.5 Practicalities
- Nobre's median was 25 min for ~4 charts with errors-only elicitation. Budget ~2–3 min per trial for B and ~4–5 min for C, so 8–12 items per participant.
- Tutorial: one worked example of the step builder on a chart that isn't used later, demonstrating "just saw it" so participants don't feel obliged to over-articulate.
- Log everything as JSON traces (§2 schema) from the start, so analysis doesn't require post-hoc coding of free text.

---

## 4. Coding open-ended / think-aloud text into the grammar

1. Segment into clauses. Your ACE pipeline already does this.
2. Label each clause with a step type, its arguments, and an error tag, using an LLM given the chart image + item reference trace. Validate on a human-coded subset (target κ ≥ .7 on step type).
3. Align to reference traces and find the first divergence.
4. **Pilot now on Nobre's 817 explanations + sketches.** Measure what fraction of trials yield ≥ 2 typed steps and how often the sketch disambiguates the extracted element. That tells you how much the existing data can carry and quantifies the gap that the new design fills.

---

## 5. Related work (process-level accounts / elicitation methods)

PDFs marked [DL] are in `../related_work/`. Grouped by which stage(s) they inform.

**Theories of the process (stages and loops)**
- Pinker 1990, *A theory of graph comprehension*: visual description → graph schema → conceptual message, with top-down re-encoding driven by the question. This is the theoretical basis for stages recurring in any order.
- Carpenter & Shah 1998, JEP:Applied: eye-tracking shows **iterative cycles** of encoding a pattern, finding its referent in the axis or legend, and interpreting it. Plot↔label gaze transitions give a direct proxy for A↔E loops.
- Shah & Hoeffner 2002; Freedman & Shah 2002 (construction-integration); Shah & Freedman 2011: prior knowledge (K) interacts with extraction rather than coming afterwards.
- Trickett & Trafton 2006: "spatial transformations" are a non-arithmetic kind of COMPUTE, found in verbal protocols.
- Ratwani, Trafton & Boehm-Davis 2008: eye-tracking + think-aloud, alternating visual clustering and integration. A methodological template for aligning gaze with speech.
- Peebles & Cheng 2003 [DL]; Lohse 1993 (UCIE): **executable step-by-step models** (ACT-R / GOMS-like) of A→E→C that predict latency and scanpaths. These are the closest existing format to a "reference trace".
- Kosslyn 1989: component taxonomy for ATTEND (framework, specifiers, labels).
- Curcio 1987; Friel, Curcio & Bright 2001: read the data / between the data / beyond the data, roughly E / C / K.
- Padilla et al. 2018: dual-process (Type 1/2) extension of Pinker; Type 2 ≈ effortful COMPUTE.
- Ullman 1984; Michal et al. 2016 [DL]; Michal & Franconeri 2017 [DL]: comparisons are **serial visual routines**, and the order of the routine predicts the verbal interpretation. This is evidence that sequence matters for the answer.

**Literacy tests and response-process evidence**
- VLAT (Lee et al. 2017), Mini-VLAT [DL], Boy et al. 2014 (IRT), CALVI [DL], A-VLAT/A-CALVI [DL]: answers only. CALVI adds coded free-text reasoning.
- Nobre et al. 2024 [DL]: see §1.
- Chang et al. 2025 [DL]: BubbleView attention maps during Mini-VLAT/CALVI. Attention patterns differ with literacy, which validates scalable A-traces.
- Schnizer 2026 [DL]: position paper on gaze process indicators (component attention, plot↔label integration rate).
- Cutler et al. 2026 [DL]: read vs. critique vs. sketch assessment modalities, relevant to the choice of elicitation format.
- Burns et al. 2020 [DL] (Bloom levels); Varona et al. 2025 [DL] (state of the art in vis literacy).
- Verma & Fan 2025 (arXiv 2505.08031): models the difficulty of questions about visualizations. Useful for item selection.
- **The agent found no published think-aloud / cognitive-interview study of VLAT items.** This is an open gap.

**Elicitation methods**
- Ericsson & Simon 1993: concurrent level-1/2 verbalization preserves process order, while asking for "why" explanations is reactive. This motivates no-"why" prompts in condition D.
- BubbleView (Kim et al. 2017) [DL]; Restricted Focus Viewer (Jansen et al. 2003): crowd-scale attention sequences.
- Borkin et al. 2016: eye-tracking AOIs by component (title/axes/legend/data). An AOI scheme to reuse.
- Goldberg & Helfman 2011: segment value-reading from gaze into find dimension → find point → read value.
- Ragan et al. 2016: provenance taxonomy, useful for logging the step-builder interactions.

**Prior knowledge (K)**
- Xiong et al. 2020 [DL] (curse of knowledge): background stories change what looks salient, so K biases A.
- McNutt et al. 2020: "Reading" mirages as K sub-labels.
- Quadri et al. 2024 [DL]: think-aloud + written takeaways with a reusable codebook. Takeaways diverge from designer intent.

**LLM angle (the same dataset could serve as a process benchmark)**
- Hong et al. 2025 [DL]: LLMs answer VLAT from priors when the data is altered (K overrides E). Bendeck & Stasko 2024 [DL]: GPT-4 is weak at E but fine at C. Charts-of-Thought (Das et al. 2025) [DL]: forcing an extract → verify → analyse decomposition helps. ChartQA [DL]: E + C questions with no traces.

