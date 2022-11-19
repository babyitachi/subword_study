import plotly.express as px
import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys
path =sys.argv[1]

with open(path,'r') as f:
    scores=json.load(f)

newScores=[]
for i in scores:
    j=".".join(i.split('.')[3:6])
    newScores.append({'config':j,'scores':scores[i],'type':j.split('.')[0]})

df = pd.DataFrame(newScores)
fig = px.scatter(df,x='config', y='scores', color='type', symbol="type")
fig.update_traces(marker_size=10)
fig.show()

fig.write_image('./marathi_ws_final.jpg')
fig.write_html('./marathi_ws_final.html')