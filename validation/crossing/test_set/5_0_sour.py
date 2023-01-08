from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cchkx = Factor("cchkx", ["thqj", "leodpv"])
bltu = Factor("bltu", ["zjmq", "xlss"])
iji = Factor("iji", ["fpn", "putj"])
cdpwgx = Factor("cdpwgx", ["rji", "tlewtx"])
qkkivh = Factor("qkkivh", ["pemet", "tgcu"])

### EXPERIMENT
design=[cchkx,bltu,iji,cdpwgx,qkkivh]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_0_0.csv"))
nr_crossings = 1
nr_factors=5
p_code_1 = 0
p_code_2 = 0
crossing = cchkx
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = bltu
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = iji
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = cdpwgx
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = qkkivh
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cchkx,bltu,iji,cdpwgx,qkkivh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
