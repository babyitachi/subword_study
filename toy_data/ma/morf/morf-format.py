words=[]
with open('../ma.sent.1m.5.word','r') as f:
    words = f.readlines()

morfs=[]
with open('../ma.sent.1m.5.morf','r') as f:
    morfs = f.readlines()

text=""
for i,j in zip(words, morfs): 
    text+=i.strip()+" "+j.strip()+"\n"

with open("../ma.sent.1m.5.morf",'w') as f:
    f.write(text)