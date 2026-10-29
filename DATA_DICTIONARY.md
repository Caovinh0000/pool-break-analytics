# Coding rules — provisional v1

One row is one actual rack. The same rack in a replay or another upload is not a second observation. Identify by event, players, round and rack number; source URLs alone are not unique match identifiers.

T0: all balls have stopped after the break and the immediate ruling is known, before the next shot, push-out, cue-ball repositioning or respotting. Use only T0 information as predictive features.

| Field | Rule |
|---|---|
| match_id / rack_no | Stable match key / rack order within actual match |
| source_url | Evidence video URL; preserve original |
| break_ts / snapshot_ts / result_ts | Video-relative break, T0 and result timestamps. UNKNOWN if unavailable. Must follow chronological order. |
| breaker / opponent / winner | Consistent player spelling; do not conflate Eklent and Kledio Kaci |
| rules_note | Break order, 1/9 on spot, box, rack type and race length; preserve year and event context |
| balls_pocketed | Object balls 1–9 pocketed on break, including a 9 subsequently respotted; exclude cue ball and balls off table |
| cue_scratch | YES/NO/UNKNOWN; cue ball pocketed on break |
| break_foul | YES/NO/UNKNOWN; any break foul. Push-out is not a foul |
| nine_pocketed | YES/NO/UNKNOWN; 9 physically pocketed on break, regardless of win or respot |
| lowest_remaining | Lowest numbered object ball at T0; special respot cases require notes |
| cue_zone | Cue-ball centre: HEAD first quarter from breaking end; MIDDLE middle half between second-diamond lines; FOOT final quarter. Exactly on a boundary = MIDDLE. Scratch/off-table = UNKNOWN |
| direct_path | CLEAR/BLOCKED/UNKNOWN: unobstructed straight cue-ball path to lowest remaining ball. This is not a potting-lane label. Choosing safety, kick or push-out alone does not prove obstruction. Confirm historical coding uses this same definition |
| rack_over_at_break | YES only if the rack is already decided by the immediate break outcome |
| breaker_win | 1 if breaker equals winner; 0 otherwise. Target, never an input |
| coverage | COMPLETE if break, post-break board and result are available; PARTIAL if any required segment is missing; UNKNOWN if coverage cannot be assessed |
| unknown_reason | Specific missing field and reason. Scratch-related geometry is structurally unavailable, different from missing video |
| notes | Observed break events and context; later events never model inputs |
| review_status / reviewed_on | Human review status/date. An automated consistency check does not constitute video verification |

Source workbook is unchanged. In v4 derived data, coverage for six collector-confirmed cut-footage racks is PARTIAL. UNKNOWN due scratch is distinct from unavailable video. Only specified fields were reviewed by the collector; source REVIEWED entries do not establish independent verification. Valid timestamps use HH:MM:SS. See METHODS.md. Only 20 sample rows are publicly provided; full observation and correction tables remain private.
