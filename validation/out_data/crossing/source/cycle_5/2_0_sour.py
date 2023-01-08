from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qqfyue = Factor("qqfyue", ["odf", "jyegq"])
quqjp = Factor("quqjp", ["zxi", "tehreq"])
ttzzfo = Factor("ttzzfo", ["bwwr", "timqo"])
wjdpdv = Factor("wjdpdv", ["kgne", "yhq"])
ggae = Factor("ggae", ["loac", "vaejq"])
igrv = Factor("igrv", ["tqy", "zcbovm"])

### EXPERIMENT
design=[qqfyue,quqjp,ttzzfo,wjdpdv,ggae,igrv]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_0_0.csv"))
nr_crossings=2
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = [qqfyue,quqjp,ttzzfo,wjdpdv]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ggae,igrv]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
