# Pool Break Analytics: development analysis

## Data and question

How does the settled post-break state relate to the breaker winning a 9-ball rack? From 500 source rows, removing duplicate M023 leaves 488 racks across 32 matches. The breaker won 305/488 (62.5%); the 95% match-bootstrap interval is 56.3–68.4%. Separate 11 racks already decided on the break, then exclude six with cut break footage. The primary sample is 471 racks, with 291 breaker wins (61.8%).

## Primary-sample results

| Group | Wins / racks | Rate | 95% match-bootstrap interval |
|---|---:|---:|---:|
| balls_pocketed: 0 | 37/90 | 41.1% | 31.5–51.9% |
| balls_pocketed: 1 | 176/259 | 68.0% | 62.4–73.1% |
| balls_pocketed: 2 | 65/105 | 61.9% | 51.8–71.2% |
| balls_pocketed: 3 | 13/17 | 76.5% | 60.0–100.0% |
| break_foul: NO | 289/442 | 65.4% | 59.4–71.4% |
| break_foul: YES | 2/29 | 6.9% | 0.0–13.9% |
| cue_zone: FOOT | 70/132 | 53.0% | 43.9–62.6% |
| cue_zone: HEAD | 47/68 | 69.1% | 54.6–82.8% |
| cue_zone: MIDDLE | 172/241 | 71.4% | 63.4–78.0% |
| cue_zone: UNKNOWN | 2/30 | 6.7% | 0.0–13.5% |
| direct_path: BLOCKED | 39/67 | 58.2% | 46.3–70.9% |
| direct_path: CLEAR | 250/374 | 66.8% | 60.3–73.2% |
| direct_path: UNKNOWN | 2/30 | 6.7% | 0.0–13.5% |

Intervals use 3,000 resamples of entire matches. Unknown geometry mostly follows scratches, not an additional table position. These are observational associations; sampling, player skill and position difficulty may differ between groups.

## Legal breaks by ball count

| Object balls pocketed | Wins / racks | Rate |
|---|---:|---:|
| 0 | 36/80 | 45.0% |
| 1 | 175/245 | 71.4% |
| 2 | 65/100 | 65.0% |
| 3 | 13/17 | 76.5% |

## Match-grouped model evaluation

Logistic regression C=1 uses five T0 features. Standardization and one-hot encoding are fitted inside each training fold. No names, notes, timestamps or winner labels are inputs.

| Model | Accuracy | Brier | Log loss | AUC |
|---|---:|---:|---:|---:|
| Training-fold rate | 61.8% | 0.236 | 0.666 | 0.478 |
| Foul only | 67.1% | 0.217 | 0.623 | 0.552 |
| Five features | 66.9% | 0.209 | 0.607 | 0.669 |

The full model improves probability error but not classification accuracy over the foul-only model. The dashboard uses a final fit on all 471 development rows, not the held-out evaluation predictions.

## Review, test and limitations

The collector resolved all 16 priority checks and reported PASS for all 50 preselected random full-row reviews. This is not independent verification. Review scope and the six missing-footage exclusions are summarized in METHODS.md; row-level histories remain private.

On the separately submitted 21-rack sample, the frozen model achieved 13/21 correct (61.9%) and Brier 0.241, versus 0.267 for the frozen foul-only baseline and 0.281 for the constant baseline. Read the separate new-match report for per-match results and the changed video sources. No retraining occurred.

The study is exploratory. Match grouping reduces within-match leakage, but does not eliminate repeated players or events. The small, selected new-match test does not establish generalization, calibration or causal effects. If its outcomes inform future modelling changes, it must become development data and another untouched set is needed.

## Data availability

Only 20 illustrative development racks are released. Full development and new-match records, row-level predictions and review histories remain private. The public sample cannot independently reproduce these aggregate results.
