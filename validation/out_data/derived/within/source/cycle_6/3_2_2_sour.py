from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
khg = Factor("khg", ["das","nef","nzdsi","mlbqzo","qlnb","quq"])
jcs = Factor("jcs", ["kojxp","nnj","kbf","hrrluj","uftz","kwakqp","dbo"])
def jnzxb(khg, jcs):
     return "mlbqzo" == khg
def vspr(khg, jcs):
     return khg != "mlbqzo" and  jcs == "hrrluj"
def gqagd(khg, jcs):
     return (not khg == "mlbqzo") and (jcs != "hrrluj")
pooq = DerivedLevel("qwzph", WithinTrial(jnzxb, [khg, jcs]))
tju = DerivedLevel("adqp", WithinTrial(vspr, [khg, jcs]))
hkbv = DerivedLevel("xxmgu", WithinTrial(gqagd, [khg, jcs]))
oxdgdz = Factor("ojj", [pooq, tju, hkbv])

### EXPERIMENT
design=[khg,jcs,oxdgdz]
crossing=[oxdgdz]
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