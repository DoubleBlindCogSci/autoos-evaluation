from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vntxvn = Factor("vntxvn", ["opt", "vvvkf"])
hiknfi = Factor("hiknfi", ["ojyy", "wry"])
dsr = Factor("dsr", ["dpl", "cup"])
cdb = Factor("cdb", ["tlxy", "fibldj"])
brtxn = Factor("brtxn", ["zrkqjj", "mpkne"])
mrmoz = Factor("mrmoz", ["uozgu", "kkur"])
jbghdj = Factor("jbghdj", ["ycb", "jom"])

### EXPERIMENT
design=[vntxvn,hiknfi,dsr,cdb,brtxn,mrmoz,jbghdj]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_7_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_7_0.csv"))
nr_crossings = 1
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = vntxvn
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = hiknfi
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = dsr
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = cdb
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = brtxn
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = mrmoz
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = jbghdj
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [vntxvn,hiknfi,dsr,cdb,brtxn,mrmoz,jbghdj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
