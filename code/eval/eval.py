import pandas as pd
import torch, numpy as np
from scipy import stats
import sys
import sklearn
from sklearn.metrics.pairwise import cosine_similarity

def getArgs():
    return sys.argv

def loadVectors(model_path):
    vecs=[]
    with open(model_path, 'r') as f:
        vecs=f.readlines()
    return vecs

def vectorize(vecs):
    vs={}
    for ind,i in enumerate(vecs):
        if ind==0:
            n,d = [int(k) for k in i.split(" ")]
        else:
            i = i.split(" ")
            key = i[0]
            val = [float(k) for k in i[1:]]
            vs[key]=val
    return n,d,vs

def getEmbb(word):
    if word in vec_dict:
        return vec_dict[word]
    np.random.seed(0)
    return np.random.random(d)

def getSims(w1,w2):
    v1=getEmbb(w1)
    v2=getEmbb(w2)
    # sp =stats.spearmanr(v1, v2)
    # cor=sp.correlation
    # return 5*(1+cor)
    sp =cosine_similarity([v1], [v2])
    return (1+sp[0][0])*5

def getModelInfo(path):
    path.split('/')

def loadModel(model_path):
    return torch.load(model_path)

if __name__=="__main__":
    args = getArgs()
    # args: eval.py src_csv_file_path model_list[model_vector_paths]_txt_file_path
    print('args', args)
    if len(args)>2:
        csv_path = args[1]
        df = pd.read_csv(csv_path)
        # df = df[['0','1','2']]
        # df.columns = ['w1', 'w2', 'score']
        # model = loadModel(path)
        vec_paths_path = args[2] #"/home/abhishrut/hsl/project/abhishrut/sw_study-master/code/outfiles/ma/morf.add.15.0.05.100000/ma.sent.1m.morf.add.ep15.lr0.05.bs100000.vec.txt"
        
        vec_paths=[]
        with open(vec_paths_path, 'r') as f:
            vec_paths=f.readlines()

        for vec_path in vec_paths:
            print(vec_path)
            vecs = loadVectors(vec_path.strip())
            n,d,vec_dict=vectorize(vecs)

            pred_score=[]
            for i,row in df.iterrows():
                pred_score.append(getSims(row['w1'], row['w2']))

            header = vec_path.split("/")[-1]
            df[header]=pred_score
        df.to_csv(csv_path) #'../../toy_data/ma/eval/marathi_ws_score.csv')

        # print(getEmbb(df['w1'][0]),getEmbb(df['w1'][1]))
        # print(vec_dict.keys())
    else:
        print('args not found')
