# Pool Break Analytics — selective public release

An exploratory study of 9-ball break outcomes, with an interactive model, English reports and **20 illustrative rack records**. The complete development and new-match datasets are retained privately.

## What is shared

- Reports, methods, four charts and aggregate evaluation results.
- `sample_data.csv`: 20 collector-reviewed development racks with source links and timestamps.
- `model.json` and `estimator.js`: the trained five-feature logistic model and its inference code.
- Python code demonstrating sample analysis and the match-grouped evaluation method.
- Synthetic estimator test combinations; these are not observed racks.

## What is not shared

The full 500-row source export, 488-row retained dataset, 471-row model cohort, 21 new-match observations, row-level predictions, review/correction logs and original Excel workbooks are not included or embedded in the website. This release cannot independently reproduce the study's full numeric results without the private records. Published reports contain aggregate results.

The browser runs the estimator locally, so the model coefficients and client-side code are visible and can be copied. This release protects access to the complete observation tables, not the model. The exact-match rack-count feature has been removed because it previously required embedding full records.

## Results at a glance

The development study used 500 source rows, reduced to 488 distinct racks from 32 matches. After separating 11 racks already decided on the break and excluding six with missing footage, the primary sample contains 471 racks. The breaker won 291/471 (61.8%).

| Evaluation | Model | Accuracy | Brier (lower is better) |
|---|---|---:|---:|
| Match-grouped cross-validation, 471 racks | Five features | 66.9% | 0.209 |
| Match-grouped cross-validation, 471 racks | Foul only | 67.1% | 0.217 |
| Frozen model, 21 new racks | Five features | 61.9% (13/21) | 0.241 |
| Frozen model, 21 new racks | Foul only | 52.4% (11/21) | 0.267 |
| Frozen model, 21 new racks | Constant development rate | 42.9% (9/21) | 0.281 |

The collector resolved 16 priority checks and reported PASS for a preselected 50-rack sample. This is self-review, not independent validation. The three new matches were selected, are a small sample, and used different submitted video IDs from the initial registration. Source changes are disclosed in the report; underlying records remain private.

## Open and run

Open `index.html` locally in a browser; no API key or paid service is required. Read `REPORT.md`, `PROJECT_SUMMARY.md`, `NEW_MATCH_REPORT.md` and `METHODS.md`.

```sh
python analyze_sample.py sample_data.csv
python -m pip install -r requirements.txt
node test_estimator.js
```

The sample command reports descriptive counts for the 20 public rows only. It does not reproduce the full study or constitute a new model test: these records come from development data. `analysis_pipeline.py` shows the grouped modelling procedure and accepts a separately supplied, already reviewed primary-cohort CSV. Running it on the sample evaluates the sample, not the private study. Never replace the frozen study model with a fit on the public sample.

## Public sample

The 20 rows are an illustrative subset of the collector-reviewed 50-rack sample, selected deterministically with seed 20261019 and at most one rack per match. They are not a representative evaluation set. Their values were copied unchanged from the reviewed development cohort.

## Authorship and interpretation

The creator designed the question, collected and reviewed labels, defined coding rules and interpreted the results. AI assisted programming, implementation and documentation. No peer review, independent video audit, causal effect or calibrated individual probability is claimed.

## Publication

Upload only this folder's contents to a fresh GitHub repository. Do not upload earlier release bundles, private records, original workbooks, or prior hosting-repository history.The project is publicly available on GitHub. No project-wide reuse license is assigned in this release. Source broadcasts are linked in the sample, not redistributed.
