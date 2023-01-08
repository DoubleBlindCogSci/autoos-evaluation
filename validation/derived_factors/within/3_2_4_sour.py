from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
voy = Factor("voy", ["vcl","wfp","jrhhib","xgzu","svmyom","kuezq","vdk"])
znaqm = Factor("znaqm", ["vcl","wfp","jrhhib","xgzu","svmyom","kuezq","vdk"])
cfyys = Factor("cfyys", ["vcl","wfp","jrhhib","xgzu","svmyom","kuezq","vdk"])
def vdzez(voy, cfyys, znaqm):
     return cfyys == voy
def opexkb(voy, cfyys, znaqm):
     return cfyys != voy and voy == znaqm
def qfsext(voy, cfyys, znaqm):
     return (not vdzez(voy, cfyys, znaqm)) and (not voy == znaqm)
zlfvvt = Factor("ckzpq", [DerivedLevel("xjx", WithinTrial(vdzez, [voy, znaqm, cfyys])), DerivedLevel("eztha", WithinTrial(opexkb, [voy, znaqm, cfyys])),DerivedLevel("mkjja", WithinTrial(qfsext, [voy, znaqm, cfyys]))])
### EXPERIMENT
design=[voy,znaqm,cfyys,zlfvvt]
crossing=[zlfvvt]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)