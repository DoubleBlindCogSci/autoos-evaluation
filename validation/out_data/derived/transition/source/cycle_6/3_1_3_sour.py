from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wov = Factor("wov", ["lgit","wxcyas","zle","rlse","kum","zkgbw"])
def ymbt(wov):
     return wov[0] == "lgit" and wov[-1] != "wxcyas"
def eooqgz(wov):
     return (not "lgit" != wov[0]) and  "wxcyas" == wov[-1]
def vexei(wov):
     return (wov[0] != "lgit") and (not wov[-1] == "wxcyas")
wvn = Factor("kuuz", [DerivedLevel("kgwv", Transition(ymbt, [wov])), DerivedLevel("jxl", Transition(eooqgz, [wov])),DerivedLevel("sfam", Transition(vexei, [wov]))])
### EXPERIMENT
design=[wov,wvn]
crossing=[wvn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)