from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mwl = Factor("mwl", ["yrk", "ftmsmd"])
wxrk = Factor("wxrk", ["zxpc", "zhd"])
vwlfs = Factor("vwlfs", ["srr", "uls"])
jxmneh = Factor("jxmneh", ["jgdtte", "trd"])
lwimrr = Factor("lwimrr", ["edykcg", "sbved"])
qmyt = Factor("qmyt", ["imqo", "lyqxsn"])
rhb = Factor("rhb", ["qurmxf", "rghx"])
fyywz = Factor("fyywz", ["zztcep", "zkmpl"])
wtwqze = Factor("wtwqze", ["yxtxif", "fqxuy"])
ijzprx = Factor("ijzprx", ["yyh", "nas"])
ghk = Factor("ghk", ["rayzdp", "ojv"])

### EXPERIMENT
design=[mwl,wxrk,vwlfs,jxmneh,lwimrr,qmyt,rhb,fyywz,wtwqze,ijzprx,ghk]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_5_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_5_0.csv"))
nr_crossings=4
nr_factors=11
p_code_1 = 0
p_code_2 = 0
crossing = [mwl,wxrk,vwlfs]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [jxmneh,lwimrr,qmyt,rhb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [fyywz,wtwqze,ijzprx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ghk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
