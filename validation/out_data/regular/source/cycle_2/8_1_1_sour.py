from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cfrhkI=Factor("E2QybeIzTbmE",[Level("Ps4solx7LQp",7),'gU2zjVj',"Mj*w%D_UzPCNCN","PSwRQC","jG4","PnChNip^E b",Level('ZQwwn',1),Level("fDr",7)])

### EXPERIMENT
design=[cfrhkI]
crossing=[cfrhkI]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_1_1_0.csv"))
nr_factors=1
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)