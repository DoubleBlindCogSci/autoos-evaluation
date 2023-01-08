from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sjige = Factor("sjige", ["bjq", "ohgb"])
pjrglr = Factor("pjrglr", ["nxqcue", "sdaqf"])
uos = Factor("uos", ["avwlf", "qfvz"])
ojj = Factor("ojj", ["zawnq", "ltqf"])
kwy = Factor("kwy", ["xdcz", "oxe"])
xyrff = Factor("xyrff", ["yaaqs", "hojas"])

### EXPERIMENT
design=[sjige,pjrglr,uos,ojj,kwy,xyrff]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_4_0.csv"))
nr_crossings=3
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = [sjige,pjrglr,uos]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ojj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [kwy,xyrff]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
