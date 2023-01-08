from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
efoaam = Factor("efoaam", ["vaw", "jytf"])
kouhiu = Factor("kouhiu", ["pswae", "pcl"])

### EXPERIMENT
design=[efoaam,kouhiu]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/1_6_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/1_6_0.csv"))
nr_crossings=1
nr_factors=2
p_code_1 = 0
p_code_2 = 0
crossing = [efoaam,kouhiu]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
