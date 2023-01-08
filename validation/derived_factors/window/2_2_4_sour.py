from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
igge = Factor("igge", ["tyd","nmmpt","dyzqcq","xkwqu","rzwhpo","grrdhv"])
xsbior = Factor("xsbior", ["dke","rfmr","vbwyr","pqp","awnmbl","wrl"])
def ddiyy(igge, xsbior):
    return igge[-1] != "xkwqu" or xsbior[0] != "wrl"
def aimnb(igge,xsbior):
    return igge[-1] == "xkwqu" and xsbior[0] == "wrl"
xttu = Factor("fofjlr", [DerivedLevel("oiuoqk", Window(ddiyy, [igge, xsbior],2,1)), DerivedLevel("alnlm", Window(aimnb, [igge, xsbior],2,1))])
### EXPERIMENT
design=[igge,xsbior,xttu]
crossing=[xttu]
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