from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RZRcs5yj=Factor(']kT',['gfno%S!y',"5Ex!Si",Level("SFuS$^dox]O",1),"JNM",'FXgs9U;xQ',"cpxjNiurae_P"])
UKx4A4WzDX=[Level('XDQm',7),'8*b2',"OVk6EQh",'{<T_aIYLJQO',"mSb0",Level("&ftzV",4)]
noyLNW=Factor("t toElWzUOfkCN",UKx4A4WzDX)

### EXPERIMENT
design=[RZRcs5yj,noyLNW]
crossing=[RZRcs5yj,noyLNW]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_1_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)