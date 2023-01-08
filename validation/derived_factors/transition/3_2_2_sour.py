from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mhlntl = Factor("mhlntl", ["bmkp","gyup","yzpve","ysj","gtxusf","nshkc"])
iqiac = Factor("iqiac", ["oiffr","yjfxkd","warzfy","uvjgcj","venv","rxz","rkbbpe","kkbhry"])
def ydenba(mhlntl, iqiac):
     return "bmkp" == mhlntl[-1] and iqiac[0] != "oiffr"
def nfqoag(mhlntl, iqiac):
     return "bmkp" != mhlntl[-1] and iqiac[0] == "oiffr"
def fbi(mhlntl, iqiac):
     return (not mhlntl[-1] == "bmkp") and (not iqiac[0] == "oiffr")
ealmpn = Factor("wua", [DerivedLevel("ifirm", Transition(ydenba, [mhlntl, iqiac])), DerivedLevel("kjv", Transition(nfqoag, [mhlntl, iqiac])),DerivedLevel("ydl", Transition(fbi, [mhlntl, iqiac]))])
### EXPERIMENT
design=[mhlntl,iqiac,ealmpn]
crossing=[ealmpn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)