from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jwovfi = Factor("jwovfi", ["khjida","bdyfep","ajxqv","wyfy","hhyd","lvff"])
wouq = Factor("wouq", ["hrfrp","yajjc","frwd","ldxil","vpy","ygs","dpvb"])
def pjpf(jwovfi, wouq):
     return "lvff" == jwovfi[-2] and not wouq[0] == "dpvb"
def nrjrft(jwovfi, wouq):
     return jwovfi[-2] != "lvff" and  wouq[0] == "dpvb"
def uvfzw(jwovfi, wouq):
     return (not jwovfi[-2] == "lvff") and (not nrjrft(jwovfi, wouq))
henb = DerivedLevel("pfim", Window(pjpf, [jwovfi, wouq],3))
fizxid = DerivedLevel("suvb", Window(nrjrft, [jwovfi, wouq],3))
pvylvp = DerivedLevel("ekb", Window(uvfzw, [jwovfi, wouq],3))
icluy = Factor("rvvq", [henb, fizxid, pvylvp])

### EXPERIMENT
design=[jwovfi,wouq,icluy]
crossing=[icluy]
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