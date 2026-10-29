# Selective release validation

Checked on 19 October 2026.

- The only observation table supplied is `sample_data.csv`: 20 unchanged records from 20 development matches. These records are illustrative and are not an independent test set.
- No complete development or new-match observation table is included in JSON, HTML or downloads. The dashboard does not embed the private row-level dataset.
- Published development counts and grouped summaries match the reviewed private analysis.
- The frozen model is unchanged. SHA-256: `561aef968f57765fd73d1d9f9f1618a74e562b7d4015e05647fc01a4ddad8ec7`.
- All 384 synthetic Python/JavaScript probability comparisons passed; maximum absolute difference was 2.22e-16.
- Mock DOM checks passed for initialization, invalid inputs, reset and foul/unknown inputs. Local report and asset references resolve.
- The sample description script and grouped cross-validation pipeline both ran successfully on the sample. Their demonstration outputs are not the study results.
- Release files were scanned for email addresses and common credential patterns. No matches were found. Original workbooks, private review logs and full prediction tables are excluded.
- The current static release replaces legacy download files. This does not erase older private hosting versions or repository history. Publish the selective ZIP in a fresh repository if sharing on GitHub.

Live browser rendering was not tested in this environment. Automated logic and asset checks do not substitute for a visual browser review.
