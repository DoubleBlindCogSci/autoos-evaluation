from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xjkwdl = Factor("xjkwdl", ["mmji","amld","kjw","cylzzt","duein","chne","zqjd","howz"])
def sdizeo(xjkwdl):
     return xjkwdl == "chne"
def utrr(xjkwdl):
     return xjkwdl == "cylzzt"
def xokmmi(xjkwdl):
     return (xjkwdl != "chne") and (not xjkwdl == "cylzzt")
gpvl = DerivedLevel("azfana", WithinTrial(sdizeo, [xjkwdl]))
supqp = DerivedLevel("eqs", WithinTrial(utrr, [xjkwdl]))
nyhivj = DerivedLevel("dnfd", WithinTrial(xokmmi, [xjkwdl]))
bhx = Factor("chqiby", [gpvl, supqp, nyhivj])

### EXPERIMENT
design=[xjkwdl,bhx]
crossing=[bhx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)