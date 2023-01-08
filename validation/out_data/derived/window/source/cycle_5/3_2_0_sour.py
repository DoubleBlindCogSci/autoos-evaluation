from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vusvwj = Factor("vusvwj", ["vbhsbt","reonc","doe","uxo","dpsf","gjsat","yac","nqplwf"])
rqpzlq = Factor("rqpzlq", ["evitfv","xfwdfh","xzjayj","vcmxu","xpsc","rkv","xfmw"])
def hyar(vusvwj, rqpzlq):
     return vusvwj[-2] == "doe" and rqpzlq[-1] != "xfwdfh"
def aduv(vusvwj, rqpzlq):
     return vusvwj[-2] != "doe" and  rqpzlq[-1] == "xfwdfh"
def auy(vusvwj, rqpzlq):
     return (not hyar(vusvwj, rqpzlq)) and (rqpzlq[-1] != "xfwdfh")
hxb = DerivedLevel("gqrznp", Window(hyar, [vusvwj, rqpzlq],3))
eajlk = DerivedLevel("fha", Window(aduv, [vusvwj, rqpzlq],3))
rlg = DerivedLevel("jkz", Window(auy, [vusvwj, rqpzlq],3))
wruaj = Factor("hkfpd", [hxb, eajlk, rlg])

### EXPERIMENT
design=[vusvwj,rqpzlq,wruaj]
crossing=[wruaj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)