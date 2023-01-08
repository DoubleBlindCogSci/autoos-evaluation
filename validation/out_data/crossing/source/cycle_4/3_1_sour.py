from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yoqjb = Factor("yoqjb", ["gvnmel", "adigy"])
nxfdg = Factor("nxfdg", ["gdknxm", "qypoor"])
cpezj = Factor("cpezj", ["hzgs", "suc"])
idyt = Factor("idyt", ["ynbdks", "osky"])
vlfhih = Factor("vlfhih", ["yaeo", "lyarl"])
cglr = Factor("cglr", ["kzhumc", "dutq"])
mhv = Factor("mhv", ["izwus", "rzes"])
yohyq = Factor("yohyq", ["tsfohq", "dghsn"])

### EXPERIMENT
design=[yoqjb,nxfdg,cpezj,idyt,vlfhih,cglr,mhv,yohyq]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0.csv"))
nr_crossings=3
nr_factors=8
p_code_1 = 0
p_code_2 = 0
crossing = [yoqjb,nxfdg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cpezj,idyt,vlfhih,cglr]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [mhv,yohyq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
