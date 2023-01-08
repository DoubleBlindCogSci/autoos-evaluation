from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xcgfv = Factor("xcgfv", ["tffb","vjlc","qayz","gsq","suinjh","pbu","zxeg"])
def akb(xcgfv):
     return xcgfv[-3] == "vjlc" and not xcgfv[0] == "vjlc"
def hyta(xcgfv):
     return xcgfv[-3] != "vjlc" and  "qayz" == xcgfv[0]
def anlv(xcgfv):
     return (not akb(xcgfv)) and (not xcgfv[0] == "qayz")
fbpa = DerivedLevel("lbxs", Window(akb, [xcgfv],4))
zow = DerivedLevel("wacr", Window(hyta, [xcgfv],4))
vukla = DerivedLevel("gvvjvb", Window(anlv, [xcgfv],4))
mzsjo = Factor("fek", [fbpa, zow, vukla])

### EXPERIMENT
design=[xcgfv,mzsjo]
crossing=[mzsjo]
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