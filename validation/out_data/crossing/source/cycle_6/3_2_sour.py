from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
csuioi = Factor("csuioi", ["vtemh", "ypyzf"])
fbjbz = Factor("fbjbz", ["tjyjs", "aifmvw"])
uweqnl = Factor("uweqnl", ["gbzrj", "dntrjv"])
xoxcg = Factor("xoxcg", ["onu", "fmlioq"])
bemrg = Factor("bemrg", ["ckast", "occul"])
hshkp = Factor("hshkp", ["zxb", "pmjch"])

### EXPERIMENT
design=[csuioi,fbjbz,uweqnl,xoxcg,bemrg,hshkp]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [uweqnl,xoxcg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [bemrg,hshkp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [csuioi,fbjbz]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 3
nr_factors = 6
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
