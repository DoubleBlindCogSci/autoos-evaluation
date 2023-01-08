from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lgbhcs = Factor("lgbhcs", ["nzay", "wmdht"])
nrkkwb = Factor("nrkkwb", ["ztwt", "iiveky"])
vcbfq = Factor("vcbfq", ["slvm", "yfagun"])
oue = Factor("oue", ["fmjdi", "bzb"])
pyihft = Factor("pyihft", ["hut", "zeqwkp"])
qng = Factor("qng", ["jtcr", "jjharn"])
hmf = Factor("hmf", ["ipx", "oiiltz"])
ozwkx = Factor("ozwkx", ["jvzx", "qmukn"])

### EXPERIMENT
design=[lgbhcs,nrkkwb,vcbfq,oue,pyihft,qng,hmf,ozwkx]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0.csv"))
nr_crossings=4
nr_factors=8
p_code_1 = 0
p_code_2 = 0
crossing = [lgbhcs,nrkkwb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [vcbfq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [oue,pyihft,qng,hmf]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ozwkx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
