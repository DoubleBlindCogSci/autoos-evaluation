from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sdsksb = Factor("sdsksb", ["eyqoh","mkgnl","osg","gum","mlgp","syfvu","wtjgfi"])
mlrmj = Factor("mlrmj", ["dyfmow","xadjr","jqukpy","eapo","hgp","ugqgfd","hiarx"])
def fnkt(sdsksb, mlrmj):
    return sdsksb[-3] != "eyqoh" and mlrmj[-1] == "xadjr"
def sxqbhj(sdsksb,mlrmj):
    return not fnkt(sdsksb, mlrmj)
nkhz = Factor("vri", [DerivedLevel("bsene", Window(fnkt, [sdsksb, mlrmj],4)), DerivedLevel("efsxc", Window(sxqbhj, [sdsksb, mlrmj],4))])
### EXPERIMENT
design=[sdsksb,mlrmj,nkhz]
crossing=[nkhz]
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