from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ejoxfm = Factor("ejoxfm", ["xszkj", "hopqq"])
mxbfc = Factor("mxbfc", ["oyfu", "raqj"])
uyo = Factor("uyo", ["jscbrn", "uuze"])
nnmaf = Factor("nnmaf", ["grywr", "vawze"])
qihvv = Factor("qihvv", ["vmbh", "kfc"])
mnjl = Factor("mnjl", ["mljq", "kdg"])

### EXPERIMENT
design=[ejoxfm,mxbfc,uyo,nnmaf,qihvv,mnjl]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_4_0.csv"))
nr_crossings=3
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = [ejoxfm,mxbfc]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [uyo,nnmaf]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qihvv,mnjl]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
