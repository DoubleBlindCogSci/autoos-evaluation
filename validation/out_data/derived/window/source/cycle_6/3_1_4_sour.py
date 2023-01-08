from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pcqwk = Factor("pcqwk", ["kpqzyd","illtb","eqvg","brs","vrjjde","awal","sqdls"])
def ldqxf(pcqwk):
     return "sqdls" == pcqwk[0] and not pcqwk[-1] == "sqdls"
def qrf(pcqwk):
     return not "sqdls" == pcqwk[0] and  "illtb" == pcqwk[-1]
def ubuiq(pcqwk):
     return (pcqwk[0] != "sqdls") and (pcqwk[-1] != "illtb")
lgtga = DerivedLevel("cysage", Window(ldqxf, [pcqwk],2))
inxh = DerivedLevel("ayui", Window(qrf, [pcqwk],2))
uxqz = DerivedLevel("tevdko", Window(ubuiq, [pcqwk],2))
gacayr = Factor("jnvu", [lgtga, inxh, uxqz])

### EXPERIMENT
design=[pcqwk,gacayr]
crossing=[gacayr]
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