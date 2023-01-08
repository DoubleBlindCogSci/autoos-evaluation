from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kcjg = Factor("kcjg", ["xal","yxlmog","nepg","nft","wdnjd","wzx","ltwgre","bbj"])
def ejzc(kcjg):
     return kcjg[0] == "wzx" and kcjg[-1] != "nft"
def snzycc(kcjg):
     return (not "wzx" != kcjg[0]) and  kcjg[-1] == "nft"
def wve(kcjg):
     return (kcjg[0] != "wzx") and (kcjg[-1] != "nft")
mhrlqc = Factor("fpzy", [DerivedLevel("ivdsvt", Transition(ejzc, [kcjg])), DerivedLevel("ngq", Transition(snzycc, [kcjg])),DerivedLevel("enjasj", Transition(wve, [kcjg]))])
### EXPERIMENT
design=[kcjg,mhrlqc]
crossing=[mhrlqc]
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