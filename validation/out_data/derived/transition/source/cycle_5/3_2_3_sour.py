from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oimbuy = Factor("oimbuy", ["zanj","byz","tcu","yhvjmi","eqmrf","aga","sykg"])
hppah = Factor("hppah", ["fiviro","eump","wmggtq","ewhvwh","glfbm","yvuvce","lsgw","skrxzy"])
def jewh(oimbuy, hppah):
     return "sykg" == oimbuy[-1] and hppah[0] != "eump"
def ctwjm(oimbuy, hppah):
     return "sykg" != oimbuy[-1] and hppah[0] == "eump"
def jxhntn(oimbuy, hppah):
     return (not oimbuy[-1] == "sykg") and (not ctwjm(oimbuy, hppah))
ppicq = Factor("pklwju", [DerivedLevel("pspk", Transition(jewh, [oimbuy, hppah])), DerivedLevel("gelwv", Transition(ctwjm, [oimbuy, hppah])),DerivedLevel("sswak", Transition(jxhntn, [oimbuy, hppah]))])
### EXPERIMENT
design=[oimbuy,hppah,ppicq]
crossing=[ppicq]
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