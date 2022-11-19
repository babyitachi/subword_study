import pandas as pd
from scipy import stats
import json
import sys

path=sys.argv[1]

df = pd.read_csv(path)

cols=list(df.columns)
score_ind = cols.index('score')

score_vec = df['score'].tolist()

score={}

for i in cols[score_ind+1:]:
    sp =stats.spearmanr(score_vec, df[i].tolist())
    cor=sp.correlation
    score[i.strip()]=cor

with open("/".join(path.split('/')[:-1])+'/marathi_ws.json','w') as f:
    json.dump(score, f)


