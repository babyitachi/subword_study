import os

path ="/".join(os.getcwd().split('/')[:-1])
path +='/outfiles/ma/'
fols = os.listdir(path)

vecs=[]
for fol in fols:
    # print(fol)
    files = os.listdir(path+fol)
    for i in files:
        if i.split('.')[-1]=='vec' or ".".join(i.split('.')[-2:-1])=='vec':
            vecs.append(path+i)

vecs="\n".join(vecs)
with open('models.txt','w') as f:
    f.writelines(vecs)