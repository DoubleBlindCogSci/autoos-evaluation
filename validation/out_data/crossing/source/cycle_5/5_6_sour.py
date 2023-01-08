from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bwmxt = Factor("bwmxt", ["gvt", "ghsy"])
smove = Factor("smove", ["abc", "tkc"])
jpbmg = Factor("jpbmg", ["gaq", "pkn"])
lkxfjb = Factor("lkxfjb", ["ndal", "swa"])
swyq = Factor("swyq", ["kucbjb", "axdka"])
eesrn = Factor("eesrn", ["iizue", "mmd"])
ypmivr = Factor("ypmivr", ["ejad", "jnle"])
zawqaf = Factor("zawqaf", ["knvfjl", "yjwu"])
erhcpb = Factor("erhcpb", ["ozjt", "phiwk"])
pdn = Factor("pdn", ["nwlbd", "xooiu"])
nyd = Factor("nyd", ["wcaujf", "bobgju"])

### EXPERIMENT
design=[bwmxt,smove,jpbmg,lkxfjb,swyq,eesrn,ypmivr,zawqaf,erhcpb,pdn,nyd]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_6_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_6_0.csv"))
nr_crossings=5
nr_factors=11
p_code_1 = 0
p_code_2 = 0
crossing = [bwmxt]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [smove,jpbmg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [lkxfjb,swyq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [eesrn,ypmivr]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zawqaf,erhcpb,pdn,nyd]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
