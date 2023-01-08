from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oqq = Factor("oqq", ["cvyjvv", "peeo"])
stvcsi = Factor("stvcsi", ["ucuap", "nas"])
uckevd = Factor("uckevd", ["mgnzg", "gdmmwm"])
hkf = Factor("hkf", ["hxpkb", "unuyg"])
xbb = Factor("xbb", ["fgzvwg", "rbbzyq"])
txbmgq = Factor("txbmgq", ["bvhsmo", "qmlnqq"])
bnarjw = Factor("bnarjw", ["sumro", "rncyug"])

### EXPERIMENT
design=[oqq,stvcsi,uckevd,hkf,xbb,txbmgq,bnarjw]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0.csv"))
nr_crossings=3
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = [oqq,stvcsi,uckevd]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [hkf,xbb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [txbmgq,bnarjw]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
