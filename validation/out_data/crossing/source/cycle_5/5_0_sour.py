from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rwkz = Factor("rwkz", ["vtddew", "rha"])
dhuwc = Factor("dhuwc", ["mklqzk", "zyquia"])
moadg = Factor("moadg", ["lpr", "cawkn"])
otjxz = Factor("otjxz", ["vlifgg", "lxpn"])
hqvz = Factor("hqvz", ["vlm", "lqjayy"])
zmrh = Factor("zmrh", ["zgd", "bppzyn"])
lwxlx = Factor("lwxlx", ["efkalb", "xjrbbf"])
cumsze = Factor("cumsze", ["emcjm", "jwyyg"])
pgsh = Factor("pgsh", ["wakkb", "bnl"])
yfmdz = Factor("yfmdz", ["rtm", "iophnl"])
azcv = Factor("azcv", ["iqnhr", "mlenr"])
sonr = Factor("sonr", ["axek", "gvhme"])
swg = Factor("swg", ["kxhb", "xoxaiz"])

### EXPERIMENT
design=[rwkz,dhuwc,moadg,otjxz,hqvz,zmrh,lwxlx,cumsze,pgsh,yfmdz,azcv,sonr,swg]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_0_0.csv"))
nr_crossings=5
nr_factors=13
p_code_1 = 0
p_code_2 = 0
crossing = [rwkz]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [dhuwc,moadg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [otjxz,hqvz,zmrh,lwxlx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cumsze,pgsh,yfmdz]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [azcv,sonr,swg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
