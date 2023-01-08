from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
opywr = Factor("opywr", ["swf", "buxg"])
cgp = Factor("cgp", ["bpji", "aqgjwe"])
tdabtp = Factor("tdabtp", ["cbb", "oowftv"])
ahdqgn = Factor("ahdqgn", ["wwf", "nzpo"])
ewo = Factor("ewo", ["xgjiui", "zqjua"])
qenbtx = Factor("qenbtx", ["chioj", "revq"])

### EXPERIMENT
design=[opywr,cgp,tdabtp,ahdqgn,ewo,qenbtx]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [cgp,tdabtp,ahdqgn,ewo]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qenbtx]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [opywr]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 3
nr_factors = 6
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
