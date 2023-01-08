from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dmjbcm = Factor("dmjbcm", ["trcg","optgu","aahlc","udmppq","kiywln","hza"])
def ixlvj(dmjbcm):
     return "kiywln" == dmjbcm[-2] and not dmjbcm[-1] == "kiywln"
def joisbh(dmjbcm):
     return dmjbcm[-2] != "kiywln" and  dmjbcm[-1] == "aahlc"
def khhps(dmjbcm):
     return (not dmjbcm[-2] == "kiywln") and (dmjbcm[-1] != "aahlc")
vzgrb = Factor("hhvfof", [DerivedLevel("aljh", Window(ixlvj, [dmjbcm],3)), DerivedLevel("mdvn", Window(joisbh, [dmjbcm],3)),DerivedLevel("qie", Window(khhps, [dmjbcm],3))])
### EXPERIMENT
design=[dmjbcm,vzgrb]
crossing=[vzgrb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)