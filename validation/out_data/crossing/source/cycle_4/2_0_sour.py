from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pfqbgl = Factor("pfqbgl", ["jjdrdd", "ihrd"])
zwpkf = Factor("zwpkf", ["wvo", "bput"])
kmidu = Factor("kmidu", ["gdcuv", "cestss"])

### EXPERIMENT
design=[pfqbgl,zwpkf,kmidu]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_0_0.csv"))
nr_crossings=2
nr_factors=3
p_code_1 = 0
p_code_2 = 0
crossing = [pfqbgl,zwpkf]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [kmidu]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
