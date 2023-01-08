from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eapq = Factor("eapq", ["vhnpdu","pbatp","lgksu","adm","lzk","xaxtof","hrtrsx"])
def bgsj(eapq):
     return "adm" == eapq[-2] and not eapq[-1] == "adm"
def qljtls(eapq):
     return not "adm" == eapq[-2] and  eapq[-1] == "hrtrsx"
def vjxrwh(eapq):
     return (not bgsj(eapq)) and (not eapq[-1] == "hrtrsx")
mxybt = DerivedLevel("bidy", Window(bgsj, [eapq],3))
stbdx = DerivedLevel("qzjjv", Window(qljtls, [eapq],3))
kobp = DerivedLevel("wpjoz", Window(vjxrwh, [eapq],3))
lxinl = Factor("xdgdqc", [mxybt, stbdx, kobp])

### EXPERIMENT
design=[eapq,lxinl]
crossing=[lxinl]
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