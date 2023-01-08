from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
qmcxwy = Factor("qmcxwy", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
jnubcb = Factor("jnubcb", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
yntx = Factor("yntx", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
def kqdgi(qmcxwy, yntx, jnubcb):
     return qmcxwy == yntx
def obds(qmcxwy, yntx, jnubcb):
     return yntx != qmcxwy and qmcxwy == jnubcb
def muki(qmcxwy, yntx, jnubcb):
     return (qmcxwy != yntx) and (qmcxwy != jnubcb)
pmpvu = DerivedLevel("lcas", WithinTrial(kqdgi, [qmcxwy, jnubcb, yntx]))
zaytav = DerivedLevel("xxk", WithinTrial(obds, [qmcxwy, jnubcb, yntx]))
lqfpkr = DerivedLevel("twq", WithinTrial(muki, [qmcxwy, jnubcb, yntx]))
mzk = Factor("iwnx", [pmpvu, zaytav, lqfpkr])

### EXPERIMENT
design=[qmcxwy,jnubcb,yntx,mzk]
crossing=[mzk]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)