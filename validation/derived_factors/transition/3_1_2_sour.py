from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gaxb = Factor("gaxb", ["vivjme","krlvjt","morfp","ospaky","cili","vpg","olw"])
def veae(gaxb):
     return gaxb[0] == "olw" and gaxb[-1] != "cili"
def etcf(gaxb):
     return (not "olw" != gaxb[0]) and  "cili" == gaxb[-1]
def safbnz(gaxb):
     return (not gaxb[0] == "olw") and (gaxb[-1] != "cili")
azbsj = Factor("pwzb", [DerivedLevel("ihbfvl", Transition(veae, [gaxb])), DerivedLevel("xtkg", Transition(etcf, [gaxb])),DerivedLevel("ffqxlr", Transition(safbnz, [gaxb]))])
### EXPERIMENT
design=[gaxb,azbsj]
crossing=[azbsj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)