from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vJZVQMrt=["Q&E$mvGpGg",'rsdDm0t',"Qam",'Jis',"ANi","EIu"]
QG2QPo_uI=Factor('_)QDVOrqBg',vJZVQMrt)
JD5fJ=Factor('t{sywPp',['{eQ',")bMciYGc&Bre",'olkYs$oeP',Level("K7YNvthvfBE>",3),'zCLQzJ<E$J','yzn[LG'])

### EXPERIMENT
design=[QG2QPo_uI,JD5fJ]
crossing=[QG2QPo_uI,JD5fJ]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_0_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)