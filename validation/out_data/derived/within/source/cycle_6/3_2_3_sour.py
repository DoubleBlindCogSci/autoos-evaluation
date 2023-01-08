from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uvga = Factor("uvga", ["sus","wveejv","dspvo","wqq","pwne","gnh"])
vinzl = Factor("vinzl", ["ida","hcf","wfw","szed","uhvpm","pwfe"])
def ovb(uvga, vinzl):
     return uvga == "wqq"
def wkg(uvga, vinzl):
     return uvga != "wqq" and  vinzl == "uhvpm"
def uon(uvga, vinzl):
     return (not uvga == "wqq") and (not vinzl == "uhvpm")
ajbcj = Factor("xtl", [DerivedLevel("sudue", WithinTrial(ovb, [uvga, vinzl])), DerivedLevel("xmjku", WithinTrial(wkg, [uvga, vinzl])),DerivedLevel("cxlk", WithinTrial(uon, [uvga, vinzl]))])
### EXPERIMENT
design=[uvga,vinzl,ajbcj]
crossing=[ajbcj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)