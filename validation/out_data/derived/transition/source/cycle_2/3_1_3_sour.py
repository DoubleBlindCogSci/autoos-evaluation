from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
fum = Factor("fum", ["vrgjb","kzdb","otqv","lqyhz","bvfjr","nfueqd"])
def dlzqg(fum):
     return "nfueqd" == fum[0] and not fum[-1] == "otqv"
def jcyiou(fum):
     return (not "nfueqd" != fum[0]) and  fum[-1] == "otqv"
def fmxqvh(fum):
     return (fum[0] != "nfueqd") and (fum[-1] != "otqv")
ieym = Factor("sfk", [DerivedLevel("gthv", Transition(dlzqg, [fum])), DerivedLevel("lyd", Transition(jcyiou, [fum])),DerivedLevel("ctzx", Transition(fmxqvh, [fum]))])
### EXPERIMENT
design=[fum,ieym]
crossing=[ieym]
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