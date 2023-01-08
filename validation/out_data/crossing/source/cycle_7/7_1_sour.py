from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fqrce = Factor("fqrce", ["juzx", "ujne"])
sncswb = Factor("sncswb", ["flsz", "lliwb"])
ugqvv = Factor("ugqvv", ["guxdq", "tottb"])
cqhdiu = Factor("cqhdiu", ["syqow", "xfyict"])
xrmn = Factor("xrmn", ["otpmc", "pepb"])
iakch = Factor("iakch", ["igoux", "wdufed"])
mytf = Factor("mytf", ["gkyk", "cknkkw"])

### EXPERIMENT
design=[fqrce,sncswb,ugqvv,cqhdiu,xrmn,iakch,mytf]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_1_0.csv"))
nr_crossings = 1
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = fqrce
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = sncswb
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = ugqvv
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = cqhdiu
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = xrmn
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = iakch
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = mytf
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [fqrce,sncswb,ugqvv,cqhdiu,xrmn,iakch,mytf]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
