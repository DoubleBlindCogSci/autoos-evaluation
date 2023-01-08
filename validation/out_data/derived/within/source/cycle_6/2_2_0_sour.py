from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oxwelr = Factor("oxwelr", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
jvns = Factor("jvns", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
swkxs = Factor("swkxs", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
def yjsjui(oxwelr, swkxs, jvns):
    return oxwelr != swkxs
def riikv(oxwelr, swkxs, jvns):
    return not (oxwelr != swkxs)
zodsp = Factor("bpso", [DerivedLevel("bzvnpz", WithinTrial(yjsjui, [oxwelr, jvns, swkxs])), DerivedLevel("trjlm", WithinTrial(riikv, [oxwelr, jvns, swkxs]))])
### EXPERIMENT
design=[oxwelr,jvns,swkxs,zodsp]
crossing=[zodsp]
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