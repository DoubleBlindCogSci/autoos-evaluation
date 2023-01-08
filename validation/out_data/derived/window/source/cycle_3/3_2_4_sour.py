from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sfjmyp = Factor("sfjmyp", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
upld = Factor("upld", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
wroo = Factor("wroo", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
def hlhwk(sfjmyp, wroo, upld):
     return sfjmyp[0] == wroo[-2] and sfjmyp[-2] != upld[0]
def ayxh(sfjmyp, wroo, upld):
     return wroo[-2] != sfjmyp[0] and sfjmyp[-2] == upld[0]
def dvnaw(sfjmyp, wroo, upld):
     return (not sfjmyp[0] == wroo[-2]) and (not sfjmyp[-2] == upld[0])
mnz = Factor("qykga", [DerivedLevel("kkgk", Window(hlhwk, [sfjmyp, upld, wroo],3)), DerivedLevel("jpv", Window(ayxh, [sfjmyp, upld, wroo],3)),DerivedLevel("wzrc", Window(dvnaw, [sfjmyp, upld, wroo],3))])
### EXPERIMENT
design=[sfjmyp,upld,wroo,mnz]
crossing=[mnz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)