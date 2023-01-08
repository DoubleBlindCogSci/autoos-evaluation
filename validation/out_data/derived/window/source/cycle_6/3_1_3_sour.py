from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ltb = Factor("ltb", ["ydna","rsx","dlpyg","zjrod","dfy","vdlgyc"])
def bjwk(ltb):
     return ltb[-1] == "dfy" and not ltb[-2] == "dfy"
def wju(ltb):
     return not "dfy" == ltb[-1] and  "ydna" == ltb[-2]
def gegwoa(ltb):
     return (ltb[-1] != "dfy") and (not wju(ltb))
acek = Factor("hva", [DerivedLevel("gziav", Window(bjwk, [ltb],3)), DerivedLevel("zldu", Window(wju, [ltb],3)),DerivedLevel("kycwij", Window(gegwoa, [ltb],3))])
### EXPERIMENT
design=[ltb,acek]
crossing=[acek]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)