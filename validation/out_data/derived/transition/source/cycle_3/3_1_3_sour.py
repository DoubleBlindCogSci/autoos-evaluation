from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ninu = Factor("ninu", ["bkkl","nxmjre","kbmc","ujbh","fge","smiik"])
def lyed(ninu):
     return ninu[0] == "nxmjre" and not ninu[-1] == "ujbh"
def jnx(ninu):
     return (not "nxmjre" != ninu[0]) and  "ujbh" == ninu[-1]
def wnt(ninu):
     return (ninu[0] != "nxmjre") and (ninu[-1] != "ujbh")
vmrl = DerivedLevel("omq", Transition(lyed, [ninu]))
jpb = DerivedLevel("fgtggu", Transition(jnx, [ninu]))
xxe = DerivedLevel("lkwyt", Transition(wnt, [ninu]))
wwzqr = Factor("jjo", [vmrl, jpb, xxe])

### EXPERIMENT
design=[ninu,wwzqr]
crossing=[wwzqr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)