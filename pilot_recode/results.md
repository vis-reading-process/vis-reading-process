# Pilot re-code results: Nobre et al. 2024 explanations → step traces

**Method.** All 817 explanations were coded from text alone into the step grammar in `CODEBOOK.md` by 6 Claude subagents, each given the chart image.
- A stratified subset of 120 trials (60 correct, 60 incorrect) was re-coded with the participant sketch added.
- 100 random trials were independently re-coded by another subagent to check reliability.
- Raw codes are in `out/`; the analysis is `analyze.py`.

**Caveats.**
- The coders are LLMs, and both reliability coders are the same model, so agreement is likely inflated relative to human coders.
- Coders split on whether a single decisive step counts as reconstructable 1 or 2. That number is softer than the step and stage counts.
- Coders were inconsistent about where stacked "read the top of the band" errors go (E1 vs D2 vs C_wrong_op). This lowers agreement with Nobre's codes.
- Several coders independently flagged possible answer-key problems: SAQ4 "Rising", ACQ4 "Constant", and some range answers.

**Headline.**
- **From text alone**, only 36% of trials are replayable and 40% have ≥ 2 typed steps. Order is evidenced in 17%, recurring loops in 1%, and prior knowledge (K) in 3%. No trial shows all 4 stages, and only 2% show ≥ 3.
- **44% of COMPUTE steps (181 of 410) are perceptual comparisons** ("Tokyo's circle is bigger"). Another 24% are trend judgements. True arithmetic is rare.
- **Sketches roughly double process recovery**: replayable 36% → 67%, Extract present 27% → 50%, error localizable on incorrect trials 35% → 70%. They add the element and the value location, not order (order hints in 3/120) and not prior knowledge (0%).
- **Agreement with Nobre's barrier codes**: only 52% on T/E/D family (κ = .25), and mostly where Nobre say E our trace puts the error in D or C. Trial-level and step-level labels diverge, and the step grammar needs sharper rules for stacked-chart errors.
- **Reliability**: stage presence κ = .70–.98, first-error family κ = .72, but only 57% of step sequences are identical.

---

Coded trials: text 817/817 (missing 0), sketch 120, reliability 100

## 1. Process information in text explanations (all trials)

| | all | incorrect | correct |
|---|---|---|---|
| N | 817 | 489 | 312 |
| median words | 11 | 11 | 11 |
| reconstructable = 0 (no process) | 17% | 21% | 12% |
| reconstructable = 1 (partial) | 47% | 48% | 45% |
| reconstructable = 2 (replayable) | 36% | 31% | 43% |
| ≥ 2 typed steps | 40% | 38% | 44% |
| mean typed steps | 1.4 | 1.4 | 1.5 |
| order evidenced | 17% | 15% | 20% |
| stage A (Attend/Encode) present | 44% | 47% | 41% |
| stage E (Extract) present | 21% | 23% | 16% |
| stage C (Compute) present | 46% | 36% | 63% |
| stage K (Know) present | 3% | 2% | 2% |
| all 4 stages present | 0% | 0% | 0% |
| ≥ 3 stages present | 2% | 2% | 2% |

Incorrect trials where the error step is localizable: **44%**

### Stage combinations

| stages | n | % |
|---|---|---|
| C | 190 | 23% |
| ∅ | 155 | 19% |
| A | 151 | 18% |
| AC | 134 | 16% |
| E | 64 | 8% |
| AE | 57 | 7% |
| EC | 34 | 4% |
| AEC | 11 | 1% |
| K | 6 | 1% |
| AK | 4 | 0% |
| EK | 4 | 0% |
| CK | 4 | 0% |

### Most common step sequences (consecutive repeats collapsed)

| sequence | n |
|---|---|
| COMPUTE | 156 |
| ATTEND | 101 |
| ∅ | 63 |
| MONITOR | 59 |
| ATTEND → COMPUTE | 57 |
| EXTRACT | 46 |
| ENCODE → COMPUTE | 35 |
| ATTEND → EXTRACT | 30 |
| EXTRACT → COMPUTE | 24 |
| PLAN | 21 |
| COMPUTE → MONITOR | 14 |
| ATTEND → MONITOR | 14 |
| ENCODE | 10 |
| MONITOR → COMPUTE | 10 |
| ATTEND → ENCODE → COMPUTE | 7 |

Traces containing a revisit/loop of a step type (e.g. ATTEND → EXTRACT → ATTEND): 1%

### Step-type totals

COMPUTE 410, ATTEND 319, EXTRACT 217, MONITOR 173, ENCODE 122, PLAN 53, ANSWER 22, KNOW 21


KNOW roles: {'sanity_check': 2, 'fill_gap': 3, 'override': 2, 'define_term': 10, 'explain': 4}

Step-level error tags: {'E1': 53, 'C_wrong_op': 38, 'D1': 22, 'D3': 22, 'D2': 20, 'E3': 20, 'T1': 14, 'E2': 12, 'E4': 12, 'T3': 11, 'T2': 7, 'C_arith': 7, 'K': 6}

### By chart (reconstructable = 2 rate)

| chart | n | replayable | no process |
|---|---|---|---|
| SA | 159.0 | 31% | 16% |
| SB | 150.0 | 42% | 19% |
| BuC | 148.0 | 33% | 20% |
| SP | 105.0 | 39% | 15% |
| SB100 | 51.0 | 43% | 16% |
| TM | 43.0 | 28% | 14% |
| AC | 41.0 | 27% | 22% |
| HC | 31.0 | 35% | 23% |
| HC2 | 29.0 | 34% | 7% |
| AC2 | 19.0 | 16% | 26% |
| LC | 17.0 | 41% | 18% |
| BC | 11.0 | 55% | 9% |
| PC | 8.0 | 50% | 25% |
| CC | 5.0 | 80% | 0% |

## 2. Step-level first error vs. Nobre trial-level barrier family (incorrect trials)

Incorrect trials with a Nobre T/E/D code: 395; of these our trace localizes an error in 51%.
 Family agreement (T/E/D, first error): **52%** (n=200); κ = 0.25

```
trace first error   C   D   E  K   T
Nobre                               
D                   8  18   9  1   3
E                  26  31  72  2   7
T                   1   5   3  1  13
```


## 3. Text-only vs. text + sketch (same 120 trials)

| | text only | text + sketch |
|---|---|---|
| replayable (=2) | 36% | 67% |
| no process (=0) | 12% | 3% |
| stage A present | 46% | 77% |
| stage E present | 27% | 50% |
| stage C present | 47% | 57% |
| stage K present | 0% | 0% |
| error localizable (incorrect, n=60) | 35% | 70% |

Reconstructability improved in 44%, unchanged 50%, lower 6%.

sketch_adds: {'element_identified': 67, 'value_location': 64, 'channel_identified': 24, 'nothing': 14, 'contradicts_text': 4, 'path_order_hint': 3}


## 4. Inter-coder reliability (100 trials, text only)

n = 100

| measure | value |
|---|---|
| κ reconstructable (0/1/2, weighted) | 0.65 |
| κ stage A present | 0.70 (agree 85%) |
| κ stage E present | 0.97 (agree 99%) |
| κ stage C present | 0.98 (agree 99%) |
| κ stage K present | 0.66 (agree 98%) |
| κ order evidenced | 0.93 |
| κ first-error family (T/E/D/C/K/none) | 0.72 |
| mean normalized edit distance of step sequences | 0.22 |
| identical collapsed sequences | 57% |
