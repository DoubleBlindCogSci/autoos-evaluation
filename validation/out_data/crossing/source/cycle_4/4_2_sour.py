from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
afmp = Factor("afmp", ["edrd", "wab"])
sewxa = Factor("sewxa", ["bubh", "nqjdez"])
zcx = Factor("zcx", ["evnaod", "bbqdgk"])
yxmeu = Factor("yxmeu", ["vauho", "sooa"])
duq = Factor("duq", ["mfvb", "iame"])
eptlj = Factor("eptlj", ["faatr", "slsw"])
mkv = Factor("mkv", ["lyzca", "dnnvx"])
rjp = Factor("rjp", ["gou", "vat"])

### EXPERIMENT
design=[afmp,sewxa,zcx,yxmeu,duq,eptlj,mkv,rjp]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0.csv"))
nr_crossings=4
nr_factors=8
p_code_1 = 0
p_code_2 = 0
crossing = [afmp,sewxa]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zcx,yxmeu,duq,eptlj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [mkv]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [rjp]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
