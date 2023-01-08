from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
txj = Factor("txj", ["qkuf","zbrskh","woqju","njhij","jjba","uotas","uzfvp"])
def gria(txj):
     return txj == "zbrskh"
def utw(txj):
     return txj == "woqju"
def bwsxmp(txj):
     return (txj != "zbrskh") and (txj != "woqju")
xxyxvk = Factor("brx", [DerivedLevel("logc", WithinTrial(gria, [txj])), DerivedLevel("lhavt", WithinTrial(utw, [txj])),DerivedLevel("wrcs", WithinTrial(bwsxmp, [txj]))])
### EXPERIMENT
design=[txj,xxyxvk]
crossing=[xxyxvk]
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