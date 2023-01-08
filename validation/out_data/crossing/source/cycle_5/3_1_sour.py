from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uugpxi = Factor("uugpxi", ["nbzjzu", "xozpwp"])
qonvzg = Factor("qonvzg", ["acln", "fhz"])
ulqva = Factor("ulqva", ["wrw", "csg"])
nsc = Factor("nsc", ["wqfa", "vote"])
tznmq = Factor("tznmq", ["oay", "frlzt"])
mdbny = Factor("mdbny", ["gesf", "ifdp"])
dyrgky = Factor("dyrgky", ["ceckb", "vbxxz"])
dtj = Factor("dtj", ["exi", "tgi"])
labfev = Factor("labfev", ["xdrh", "fco"])

### EXPERIMENT
design=[uugpxi,qonvzg,ulqva,nsc,tznmq,mdbny,dyrgky,dtj,labfev]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0.csv"))
nr_crossings=3
nr_factors=9
p_code_1 = 0
p_code_2 = 0
crossing = [uugpxi,qonvzg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ulqva,nsc,tznmq,mdbny]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [dyrgky,dtj,labfev]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
