"""Demonstrate match-grouped evaluation on a separately supplied reviewed cohort.
The public 20-row sample does NOT reproduce the published full-study results.
No networking, uploads or embedded private observations.
"""
import csv,json,sys
from pathlib import Path
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.metrics import accuracy_score,brier_score_loss,log_loss,roc_auc_score

def evaluate(path):
 with open(path,newline='') as handle:rows=list(csv.DictReader(handle))
 if not rows:raise ValueError('No observation rows supplied.')
 if len({(r['match_id'],r['rack_no']) for r in rows})!=len(rows):raise ValueError('Duplicate rack key.')
 for r in rows:
  if r['coverage']!='COMPLETE' or r['rack_over_at_break']!='NO':raise ValueError('Supply an already reviewed, eligible ongoing-rack cohort; do not silently infer missing T0 evidence.')
  if int(r['breaker_win'])!=int(r['breaker']==r['winner']):raise ValueError('Inconsistent outcome label.')
 cats=['break_foul','cue_zone','direct_path','lowest_remaining']
 X=np.array([[float(r['balls_pocketed'])]+[r[c] for c in cats] for r in rows],dtype=object)
 y=np.array([int(r['breaker_win']) for r in rows]);g=np.array([r['match_id'] for r in rows])
 if len(set(g))<5:raise ValueError('Five-fold grouped evaluation requires at least five matches.')
 pp={k:np.zeros(len(rows)) for k in ['five_features','foul_only','training_fold_rate']}
 for tr,te in GroupKFold(n_splits=5).split(X,y,g):
  assert not set(g[tr])&set(g[te])
  if len(set(y[tr]))<2:raise ValueError('A training fold has only one outcome class.')
  for name in ['five_features','foul_only']:
   pre=ColumnTransformer([('category',OneHotEncoder(handle_unknown='ignore'),[1])]) if name=='foul_only' else ColumnTransformer([('number',StandardScaler(),[0]),('category',OneHotEncoder(handle_unknown='ignore'),[1,2,3,4])])
   fit=make_pipeline(pre,LogisticRegression(C=1,max_iter=2000));fit.fit(X[tr],y[tr]);pp[name][te]=fit.predict_proba(X[te])[:,1]
  pp['training_fold_rate'][te]=y[tr].mean()
 def metrics(p):return {'accuracy':accuracy_score(y,p>=.5),'brier':brier_score_loss(y,p),'log_loss':log_loss(y,p,labels=[0,1]),'auc':roc_auc_score(y,p) if len(set(y))==2 else None}
 return {'input_file':Path(path).name,'n':len(rows),'matches':len(set(g)),'scope':'Results describe only the supplied cohort. The full private study cannot be reproduced from the public sample.','metrics':{k:metrics(v) for k,v in pp.items()}}
if __name__=='__main__':
 if len(sys.argv)!=2:raise SystemExit('Usage: python analysis_pipeline.py reviewed_primary_cohort.csv')
 print(json.dumps(evaluate(sys.argv[1]),indent=2))
