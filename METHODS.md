# Methods and data availability

## Study design

One observation is one actual 9-ball rack. Remove one duplicate match from 500 source rows to retain 488 development racks from 32 matches. Separate 11 racks decided on the break; exclude six ongoing racks with unavailable break/post-break footage. The primary cohort contains 471 racks.

At T0, all balls have settled after the break and before another stroke, push-out or repositioning. Inputs are object-ball count, break foul, cue-ball zone, direct path and lowest remaining ball. Player identities, timestamps, notes, push-out decisions and outcomes are not inputs. See DATA_DICTIONARY.md.

## Data review

Collector review resolved 16 priority checks (3 confirmed, 7 corrected, 6 missing footage) and reported full-row PASS for a preselected random sample of 50 development racks. This is self-review. An independent video audit has not occurred. Correction histories are kept privately; six missing-footage records remain outside the primary cohort.

## Modelling

Logistic regression C=1, max_iter=2000; standardize the ball count and one-hot encode the remaining four features. Five-fold GroupKFold keeps entire matches together; fit every transformation within the training fold. Evaluate accuracy at 0.5, Brier, log loss and AUC. Compare with a training-fold mean and a foul-only logistic model. Rate intervals use 3,000 resamples of entire matches, seed 20261017.

The website uses the final fit on all 471 primary rows, not OOF predictions. Both the model and inference code are public. The complete observation table is not embedded.

## Additional-match evaluation

The final model and baselines were frozen before the collector submitted 21 eligible racks from three further matches. No tuning or refitting occurred. The collector used different video IDs from the initial registration; this source deviation is disclosed and stored in private records. The three exact player-name pairs were absent from development data, but match identity and labels were not independently video-verified. No blinded collection is claimed.

## Public demonstration and limits

Twenty reviewed development records are released for inspection, not as an evaluation sample. The full analysis is not independently reproducible from these rows. analysis_pipeline.py demonstrates the model-evaluation method but cannot recreate published results without the complete reviewed cohort.

The selected professional-match sample, repeated players/events, common collector and small additional-match test limit generalization. Neither causal effects nor individual probability calibration is established. Informal push-out calculations are separate explorations, not model features or primary findings.
