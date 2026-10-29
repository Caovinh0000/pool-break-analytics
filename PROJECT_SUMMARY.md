# Pool Break Analytics

## What can the break tell us about winning a 9-ball rack?

A successful break is more than a ball falling into a pocket. It also leaves a cue-ball position, a route to the next object ball and, sometimes, a difficult decision. This project examines how those immediate conditions relate to the breaker eventually winning the rack.

The development dataset began with 500 manually collected video observations. Removing a duplicate match left 488 distinct racks from 32 matches. Eleven racks already decided on the break were separated, and six with missing break footage were excluded from modelling. The primary analysis therefore uses 471 racks. Source links, timestamps, coding rules and correction records make the observations inspectable. The collector resolved 16 priority checks and reported PASS for a preselected 50-rack review sample; no independent audit has been completed.

The breaker won 61.8% of the primary sample. Break fouls showed the clearest difference: the observed win rate was 65.4% without a foul and 6.9% with one. Among legal breaks, dry breaks won 45.0% and one-ball breaks 71.4%. The two-ball group did not outperform the one-ball group. These differences describe the sample; they do not show that changing one feature would cause a particular improvement.

A logistic regression model estimates win probability from five post-break features. Match-grouped cross-validation prevents racks from the same match appearing in both the training and test portions of a fold. The full model reached 66.9% accuracy, compared with 67.1% for a foul-only model, but reduced Brier probability error from about 0.217 to 0.209. The additional features improved one measure of probability quality without improving classification accuracy.

The model was then frozen and tested on 21 racks from three additional matches. It predicted 13 correctly (61.9%) and achieved a Brier score of 0.241, compared with 0.267 for the frozen foul-only model and 0.281 for a constant development-rate baseline. No retraining occurred. The submission used different video IDs from those registered initially; both sets of sources are retained in the evaluation record.

This is a useful early result, not a validated forecasting system. The three new matches were selected rather than randomly sampled, and their labels came from the same collector. The dataset chiefly represents televised professional play, and probability calibration has not been established. The project provides an inspectable 20-rack sample, documented methods, aggregate model comparisons and a local interactive dashboard. Full records are kept privately, so the public release does not support full independent reproduction. Further work should focus on independent label review and new matches kept separate before model changes are made.
