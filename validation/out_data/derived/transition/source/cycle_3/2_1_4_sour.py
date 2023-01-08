from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xupuds = Factor("xupuds", ["zflxlt","vbwp","rrrc","nkfv","yijpy","hbqcw"])
def ddpmdw(xupuds):
    return xupuds[0] == "nkfv" and xupuds[-1] != "zflxlt"
def gekzjl(xupuds):
    return xupuds[0] != "nkfv" or not (xupuds[-1] != "zflxlt")
ajbovd = DerivedLevel("jpetbu", Transition(ddpmdw, [xupuds]))
gagik = DerivedLevel("ilpxk", Transition(gekzjl, [xupuds]))
blapn = Factor("tmxfqu", [ajbovd, gagik])

### EXPERIMENT
design=[xupuds,blapn]
crossing=[blapn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)