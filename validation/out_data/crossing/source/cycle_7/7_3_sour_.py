from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pzdf = Factor("pzdf", ["sum", "rrv"])
drzdl = Factor("drzdl", ["cfs", "ahnsy"])
aeuu = Factor("aeuu", ["ryhl", "pwple"])
utwt = Factor("utwt", ["uulf", "kpoi"])
demlcv = Factor("demlcv", ["paeed", "yanx"])
dzhrj = Factor("dzhrj", ["qtsvi", "vfcr"])
zxtc = Factor("zxtc", ["btlsdv", "fgybf"])

### EXPERIMENT
design=[pzdf,drzdl,aeuu,utwt,demlcv,dzhrj,zxtc]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_3_0.csv"))
nr_crossings = 1
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = [pzdf,drzdl,aeuu,utwt,demlcv,dzhrj,zxtc]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
