from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
spa = Factor("spa", ["nouxqd","rvf","iuy","cnbp","arllcs","gioiz"])
def zejlc(spa):
     return "iuy" == spa[0] and spa[-1] != "gioiz"
def adiz(spa):
     return (not "iuy" != spa[0]) and  spa[-1] == "gioiz"
def ygmul(spa):
     return (not spa[0] == "iuy") and (spa[-1] != "gioiz")
dua = DerivedLevel("uudtil", Transition(zejlc, [spa]))
bgq = DerivedLevel("pvec", Transition(adiz, [spa]))
wufdvg = DerivedLevel("aeshf", Transition(ygmul, [spa]))
ozig = Factor("fnugna", [dua, bgq, wufdvg])

### EXPERIMENT
design=[spa,ozig]
crossing=[ozig]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)