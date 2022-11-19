from bpemb import BPEmb
bpemb_en = BPEmb(lang="mr")

words=""
with open('../ma.sent.1m.5.word','r') as f:
    words=f.readlines()

# words=words.split(" ")

bpes=[]
for i in words:
    bpes.append(i.strip()+" :: "+" - ".join([k.strip() for k in bpemb_en.encode(i)])[1:])
print(bpes[0])
with open('../ma.sent.1m.5.bpe','w') as f:
    f.write("\n".join(bpes))