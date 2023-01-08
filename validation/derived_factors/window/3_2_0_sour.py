from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qbr = Factor("qbr", ["oze","wuxugm","whq","guj","uqicr","mycich","juuhx","axhc"])
lpnhi = Factor("lpnhi", ["iwrg","nkk","upqzq","iyeis","lslmc","kpl","hmhisr","yfqa"])
def uednih(qbr, lpnhi):
     return qbr[0] == "oze" and lpnhi[-1] != "hmhisr"
def apzwj(qbr, lpnhi):
     return "oze" != qbr[0] and  lpnhi[-1] == "hmhisr"
def arawt(qbr, lpnhi):
     return (not uednih(qbr, lpnhi)) and (not apzwj(qbr, lpnhi))
csugv = DerivedLevel("kdby", Window(uednih, [qbr, lpnhi],2,1))
klszcv = DerivedLevel("ucb", Window(apzwj, [qbr, lpnhi],2,1))
qyyr = DerivedLevel("tnqpc", Window(arawt, [qbr, lpnhi],2,1))
xvhmxl = Factor("odsxra", [csugv, klszcv, qyyr])

### EXPERIMENT
design=[qbr,lpnhi,xvhmxl]
crossing=[xvhmxl]
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