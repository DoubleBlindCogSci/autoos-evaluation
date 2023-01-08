from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
izs = Factor("izs", ["ubcopp", "lkyv"])
hzgyu = Factor("hzgyu", ["mjt", "fsq"])
wozdzq = Factor("wozdzq", ["nxn", "wfqkyb"])
gfq = Factor("gfq", ["zdhgcp", "bgogqj"])
wmnza = Factor("wmnza", ["qpzh", "rpjvzm"])
nuvyka = Factor("nuvyka", ["cmfdmb", "cikeev"])
ezxzj = Factor("ezxzj", ["miimq", "oaaut"])

### EXPERIMENT
design=[izs,hzgyu,wozdzq,gfq,wmnza,nuvyka,ezxzj]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_0.csv"))
nr_crossings=2
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = [izs,hzgyu,wozdzq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [gfq,wmnza,nuvyka,ezxzj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
