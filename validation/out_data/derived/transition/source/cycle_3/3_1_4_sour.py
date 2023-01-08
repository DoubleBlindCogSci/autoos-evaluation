from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nwk = Factor("nwk", ["fvnll","joayyf","hump","img","muti","pncppn","fwkjs","vkfvf"])
def uffmti(nwk):
     return nwk[0] == "hump" and not nwk[-1] == "pncppn"
def xup(nwk):
     return (not "hump" != nwk[0]) and  nwk[-1] == "pncppn"
def rsuir(nwk):
     return (not uffmti(nwk)) and (not nwk[-1] == "pncppn")
owo = DerivedLevel("boqyr", Transition(uffmti, [nwk]))
qapv = DerivedLevel("xfme", Transition(xup, [nwk]))
gghw = DerivedLevel("ppjfl", Transition(rsuir, [nwk]))
ybtlj = Factor("twha", [owo, qapv, gghw])

### EXPERIMENT
design=[nwk,ybtlj]
crossing=[ybtlj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)