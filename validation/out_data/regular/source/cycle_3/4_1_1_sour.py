from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
i2LnESDU3yZ=[Level("oGwkbvwv2Y",7),Level("zfD",4),"lAd",Level("VRRkSzB2ShWhng",4)]
hJxWX2NiY9=Factor("bG*eJ%xLr",i2LnESDU3yZ)

### EXPERIMENT
design=[hJxWX2NiY9]
crossing=[hJxWX2NiY9]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_1_0.csv"))
nr_factors=1
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)