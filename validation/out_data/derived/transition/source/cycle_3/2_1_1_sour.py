from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
apgpx = Factor("apgpx", ["yjpav","hjyr","bfn","yvhm","hdfrzu","oyg"])
def letko(apgpx):
    return apgpx[0] == "hdfrzu" or apgpx[-1] == "yvhm"
def rhse(apgpx):
    return not letko(apgpx)
dhxk = Factor("ltb", [DerivedLevel("euacj", Transition(letko, [apgpx])), DerivedLevel("ctra", Transition(rhse, [apgpx]))])
### EXPERIMENT
design=[apgpx,dhxk]
crossing=[dhxk]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)