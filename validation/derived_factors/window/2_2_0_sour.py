from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zywlx = Factor("zywlx", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
vtdezu = Factor("vtdezu", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
ardkv = Factor("ardkv", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
def hzoc(zywlx, ardkv, vtdezu):
    return zywlx[0] == ardkv[-2]
def slwu(zywlx, ardkv, vtdezu):
    return not hzoc(zywlx, ardkv, vtdezu)
xwiea = Factor("sztux", [DerivedLevel("rjsv", Window(hzoc, [zywlx, vtdezu, ardkv],3,1)), DerivedLevel("kem", Window(slwu, [zywlx, vtdezu, ardkv],3,1))])
### EXPERIMENT
design=[zywlx,vtdezu,ardkv,xwiea]
crossing=[xwiea]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)