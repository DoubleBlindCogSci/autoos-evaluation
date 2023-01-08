from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tviioo = Factor("tviioo", ["nvcdsd", "qhscon"])
jur = Factor("jur", ["zuzw", "jvgu"])
ptv = Factor("ptv", ["bkk", "pihi"])
xib = Factor("xib", ["nta", "ifxes"])
zxrd = Factor("zxrd", ["thqgwf", "noj"])
imte = Factor("imte", ["uaj", "mvtkat"])
srhgs = Factor("srhgs", ["ftsmsq", "hjwij"])

### EXPERIMENT
design=[tviioo,jur,ptv,xib,zxrd,imte,srhgs]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_0.csv"))
nr_crossings=2
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = [tviioo,jur,ptv]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [xib,zxrd,imte,srhgs]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
