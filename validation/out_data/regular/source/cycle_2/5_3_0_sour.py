from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OOyj=Factor("FcUlGzASLNKP(v",[Level('Zo$b<?LHZYsw',7),'BERk[mgcl',Level("mcmW!~OZqd",8),Level('RHkFRhKFB',2),'tdHW#Ug7mCJTF'])
wddC51=Factor('aG9iGruiEpi',["{ 1N",'eNhfUe MH4gx',"W:L#SLKyD df",Level("HU0PWfKY|)",10),'qiRL'])
DKKZQXmZZH=Factor("b]arlTT",[Level('hR%q',3),Level('9Os_',7),'5U|SQ',Level("Gxu",5),'fnaZmSKA6'])

### EXPERIMENT
design=[OOyj,wddC51,DKKZQXmZZH]
crossing=[OOyj,wddC51,DKKZQXmZZH]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_0_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)