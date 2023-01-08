from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cjvn = Factor("cjvn", ["wysk","rqwpcs","jip","znmw","qzd","qnxon","luadp","pzlnoo"])
vhvm = Factor("vhvm", ["mll","uqshnl","syoqcq","zgxlr","gzrkh","wuuycd","xwx"])
def aci(cjvn, vhvm):
     return cjvn == "rqwpcs"
def cydha(cjvn, vhvm):
     return "rqwpcs" != cjvn and  vhvm == "syoqcq"
def tzejv(cjvn, vhvm):
     return (not aci(cjvn, vhvm)) and (not cydha(cjvn, vhvm))
pfqyn = DerivedLevel("kwpf", WithinTrial(aci, [cjvn, vhvm]))
vilmk = DerivedLevel("kyrs", WithinTrial(cydha, [cjvn, vhvm]))
qxhyw = DerivedLevel("ybmuj", WithinTrial(tzejv, [cjvn, vhvm]))
kdzcea = Factor("uogby", [pfqyn, vilmk, qxhyw])

### EXPERIMENT
design=[cjvn,vhvm,kdzcea]
crossing=[kdzcea]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)