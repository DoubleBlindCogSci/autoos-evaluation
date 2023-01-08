from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bvtzbp = Factor("bvtzbp", ["rst","bwcyv","rni","rszxy","cqo","zdqj","dbyspg"])
ylmywb = Factor("ylmywb", ["wviclj","cyan","zxqip","fhahdx","wzhfp"])
def uptknt(bvtzbp, ylmywb):
    return bvtzbp[-2] == "zdqj" and ylmywb[-1] != "wviclj"
def wvqu(bvtzbp,ylmywb):
    return not uptknt(bvtzbp, ylmywb)
eley = Factor("xbgs", [DerivedLevel("lxs", Window(uptknt, [bvtzbp, ylmywb],3)), DerivedLevel("gpjys", Window(wvqu, [bvtzbp, ylmywb],3))])
### EXPERIMENT
design=[bvtzbp,ylmywb,eley]
crossing=[eley]
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