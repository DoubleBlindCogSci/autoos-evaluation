from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ephyg = Factor("ephyg", ["klxa","chgc","vcnwcv","ofycwv","zctxz","xvikon","fsp"])
def khluue(ephyg):
     return "ofycwv" == ephyg[0] and not ephyg[-1] == "ofycwv"
def fmlw(ephyg):
     return not "ofycwv" == ephyg[0] and  "vcnwcv" == ephyg[-1]
def cmshgu(ephyg):
     return (not khluue(ephyg)) and (not ephyg[-1] == "vcnwcv")
wwpsay = DerivedLevel("pxky", Window(khluue, [ephyg],2))
vsiv = DerivedLevel("bcsghi", Window(fmlw, [ephyg],2))
ujz = DerivedLevel("gmpmeb", Window(cmshgu, [ephyg],2))
zwphls = Factor("ulhgwg", [wwpsay, vsiv, ujz])

### EXPERIMENT
design=[ephyg,zwphls]
crossing=[zwphls]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)