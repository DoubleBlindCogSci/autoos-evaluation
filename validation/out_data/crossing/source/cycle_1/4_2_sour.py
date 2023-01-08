from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
dfs = Factor("dfs", ["wjj", "psvjy"])
nctkh = Factor("nctkh", ["zmdkd", "ump"])
bwnmf = Factor("bwnmf", ["kxqz", "bbd"])
omlk = Factor("omlk", ["wqhkga", "axe"])
jtt = Factor("jtt", ["zubxad", "tilcb"])
cgwwdx = Factor("cgwwdx", ["guyzoj", "tbailw"])
uue = Factor("uue", ["wwgq", "epos"])
yjipe = Factor("yjipe", ["trldo", "lapfm"])
zzwjf = Factor("zzwjf", ["xigl", "iibs"])
qkf = Factor("qkf", ["wiucq", "rwgj"])
kmwsue = Factor("kmwsue", ["dgi", "deiu"])
tluxqs = Factor("tluxqs", ["pnrg", "ktzn"])
jxuc = Factor("jxuc", ["ggzan", "urid"])

### EXPERIMENT
design=[dfs,nctkh,bwnmf,omlk,jtt,cgwwdx,uue,yjipe,zzwjf,qkf,kmwsue,tluxqs,jxuc]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0.csv"))
nr_crossings=4
nr_factors=13
p_code_1 = 0
p_code_2 = 0
crossing = [dfs,nctkh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [bwnmf,omlk,jtt]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cgwwdx,uue,yjipe,zzwjf]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qkf,kmwsue,tluxqs,jxuc]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
