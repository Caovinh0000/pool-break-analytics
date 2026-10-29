"""Describe public sample rows; this is not the full study or a holdout test."""
import csv,json,sys
from collections import Counter
from pathlib import Path
path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('sample_data.csv')
with open(path,newline='') as handle:rows=list(csv.DictReader(handle))
assert len({(r['match_id'],r['rack_no']) for r in rows})==len(rows)
for r in rows:assert int(r['breaker_win'])==int(r['breaker']==r['winner'])
wins=sum(int(r['breaker_win']) for r in rows)
print(json.dumps({'scope':'Illustrative public development sample only; not a reproduction of full-study results.','racks':len(rows),'matches':len({r['match_id'] for r in rows}),'breaker_wins':wins,'breaker_win_rate':wins/len(rows) if rows else None,'break_fouls':dict(Counter(r['break_foul'] for r in rows))},indent=2))
