from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
apc = Factor("apc", ["rsh", "stbpj"])
oty = Factor("oty", ["gtihuv", "pbbq"])
lnks = Factor("lnks", ["xokq", "xww"])
llxhe = Factor("llxhe", ["qcdhca", "dcbbyj"])
ihdk = Factor("ihdk", ["hihj", "iqdq"])
pmewud = Factor("pmewud", ["pwhpfv", "ltcxjx"])
svxcxx = Factor("svxcxx", ["ludo", "tzfubv"])
zvn = Factor("zvn", ["vii", "foaf"])

### EXPERIMENT
design=[apc,oty,lnks,llxhe,ihdk,pmewud,svxcxx,zvn]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0.csv"))
nr_crossings=4
nr_factors=8
p_code_1 = 0
p_code_2 = 0
crossing = [apc,oty]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [lnks,llxhe]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ihdk,pmewud]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [svxcxx,zvn]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
