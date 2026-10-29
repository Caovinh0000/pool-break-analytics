# Frozen-model evaluation: three new matches

## Scope

The collector submitted 21 observed racks: T001 Melling–Strickland (7), T002 Atencio–Hoang (6), and T003 Kaci–Labutis (8). The 99 unfilled template slots are not observations. All 21 observed racks met the recorded eligibility checks. The breaker won 9/21 (42.9%). The original frozen model and baseline hashes match the registration. No model fitting or threshold selection took place.

## Pooled results

| Model | Correct / racks | Accuracy | Brier | Log loss | AUC |
|---|---:|---:|---:|---:|---:|
| Five features | 13/21 | 61.9% | 0.241 | 0.708 | 0.699 |
| Foul only | 11/21 | 52.4% | 0.267 | 0.735 | 0.569 |
| Constant development rate | 9/21 | 42.9% | 0.281 | 0.756 | 0.500 |

The full model predicted two more racks correctly than the foul-only model and reduced Brier by about 0.026. This describes this sample, not a confirmed improvement across future matches.

## Per-match results

| Match | Racks | Full model correct | Full-model Brier | Foul-only Brier | Constant Brier |
|---|---:|---:|---:|---:|---:|
| T001 | 7 | 6/7 | 0.195 | 0.256 | 0.314 |
| T002 | 6 | 3/6 | 0.217 | 0.222 | 0.225 |
| T003 | 8 | 4/8 | 0.301 | 0.310 | 0.293 |

The full model has lower Brier than the foul-only model in all three matches, but is worse than the constant baseline in T003. Its classification accuracy is 6/7 in T001 and 50% in each of the other matches.

## Evidence and limits

All submitted rack keys are unique; breaker_win agrees with the named winner and breaker, and recorded timestamps are chronological. These are logical checks, not an independent video audit. The three exact player-name pairs do not occur in development data, and the collector marked the matches as non-duplicates.

All three submitted video IDs differ from those registered in the initial worksheet. The original registration is retained, and the private source record retains both sets of URLs. The analysis has not independently confirmed that each replacement upload represents the same registered match. Results are therefore an exploratory evaluation of the submitted matches, with a source deviation, rather than strict confirmation of the originally registered videos.

There are four break fouls in 21 racks (19.0%), compared with 29/471 (6.2%) in development. All three matches are recorded as Premier League Pool with alternate breaks. Selection, format and a common collector limit the evaluation. Whether the collector already knew match outcomes is unknown; no blinded collection is claimed. Twenty-one racks from three matches are not 21 fully independent observations. No significance claim is made.

## Data availability

The 21 individual new-match observations and predictions are not released. Only pooled and per-match aggregate metrics are public. The frozen development estimator remains available, but this report cannot be independently reproduced without the private test records.
