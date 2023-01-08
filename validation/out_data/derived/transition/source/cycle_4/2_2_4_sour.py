from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mdl = Factor("mdl", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
xxksa = Factor("xxksa", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
ofn = Factor("ofn", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
def srrzs(mdl, xxksa, ofn):
    return mdl[0] == xxksa[-1]
def cmwdc(mdl, xxksa, ofn):
    return not srrzs(mdl, xxksa, ofn)
pcxcv = Factor("khgdqa", [DerivedLevel("ursslu", Transition(srrzs, [mdl, xxksa, ofn])), DerivedLevel("bxa", Transition(cmwdc, [mdl, xxksa, ofn]))])
### EXPERIMENT
design=[mdl,xxksa,ofn,pcxcv]
crossing=[pcxcv]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)