from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hruxe = Factor("hruxe", ["ejbn","vblag","ksrq","epttpg","uyp","mooj","zwqnb","yojs"])
whb = Factor("whb", ["bxz","wwmca","ixvf","wod","dzxlz","rwip","kmf","bpt"])
def zyi(hruxe, whb):
     return hruxe[-1] == "ejbn" and whb[0] != "ixvf"
def xkwzk(hruxe, whb):
     return hruxe[-1] != "ejbn" and whb[0] == "ixvf"
def jgutjj(hruxe, whb):
     return (not zyi(hruxe, whb)) and (whb[0] != "ixvf")
undztl = Factor("ftubtu", [DerivedLevel("mzyagu", Transition(zyi, [hruxe, whb])), DerivedLevel("mlgu", Transition(xkwzk, [hruxe, whb])),DerivedLevel("glezlm", Transition(jgutjj, [hruxe, whb]))])
### EXPERIMENT
design=[hruxe,whb,undztl]
crossing=[undztl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)