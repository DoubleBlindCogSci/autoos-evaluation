from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cgsctx = Factor("cgsctx", ["urxz", "tbnjy"])
vldij = Factor("vldij", ["kkj", "dadlvm"])
jqi = Factor("jqi", ["nzdde", "yovxbj"])
dzna = Factor("dzna", ["tbre", "xmw"])
pwc = Factor("pwc", ["jfy", "wip"])
zfd = Factor("zfd", ["kkr", "mob"])
bvwrxd = Factor("bvwrxd", ["qkthp", "qmwb"])
tuswt = Factor("tuswt", ["kkgj", "uxetk"])
kmly = Factor("kmly", ["udzl", "nkcde"])

### EXPERIMENT
design=[cgsctx,vldij,jqi,dzna,pwc,zfd,bvwrxd,tuswt,kmly]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_4_0.csv"))
nr_crossings=5
nr_factors=9
p_code_1 = 0
p_code_2 = 0
crossing = [cgsctx,vldij]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [jqi,dzna,pwc]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zfd,bvwrxd]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tuswt]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [kmly]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
