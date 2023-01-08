from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qrb = Factor("qrb", ["xmtxcu", "cizamj"])
xwscf = Factor("xwscf", ["ngub", "ljl"])
lvjonx = Factor("lvjonx", ["vgsw", "pnf"])
asnc = Factor("asnc", ["ynvzu", "jsl"])
vivr = Factor("vivr", ["zvgmw", "lab"])
qlaijq = Factor("qlaijq", ["ndxln", "sgkm"])
hovzo = Factor("hovzo", ["ntsk", "hltpm"])
udek = Factor("udek", ["irz", "yttx"])
vztuzg = Factor("vztuzg", ["qqiyjm", "harqsn"])

### EXPERIMENT
design=[qrb,xwscf,lvjonx,asnc,vivr,qlaijq,hovzo,udek,vztuzg]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0.csv"))
nr_crossings=4
nr_factors=9
p_code_1 = 0
p_code_2 = 0
crossing = [qrb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [xwscf,lvjonx,asnc]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [vivr,qlaijq,hovzo,udek]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [vztuzg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
