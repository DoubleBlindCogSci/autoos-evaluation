from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnwfqb = Factor("cnwfqb", ["ccfbvf","wwufgu","zoijaj","rhmmot","oenx","ovdxg"])
hbb = Factor("hbb", ["hakfyy","znz","nmw","ookaqo","uocjno","xgsl"])
def pri(cnwfqb, hbb):
    return cnwfqb[0] == "rhmmot" and hbb[-1] != "uocjno"
def jkl(cnwfqb,hbb):
    return not (cnwfqb[0] == "rhmmot") or hbb[-1] == "uocjno"
slfnkn = DerivedLevel("qnu", Transition(pri, [cnwfqb, hbb]))
ylr = DerivedLevel("axqan", Transition(jkl, [cnwfqb, hbb]))
apx = Factor("uogeig", [slfnkn, ylr])

### EXPERIMENT
design=[cnwfqb,hbb,apx]
crossing=[apx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)