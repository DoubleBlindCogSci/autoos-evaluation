from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hwcri = Factor("hwcri", ["hipky","uwsc","cpkgs","ghvkz","kwxymw","vpz","xgg"])
def puj(hwcri):
     return hwcri[0] == "kwxymw" and not hwcri[-1] == "xgg"
def vtnkc(hwcri):
     return (hwcri[0] != "kwxymw") and  "xgg" == hwcri[-1]
def oohktt(hwcri):
     return (hwcri[0] != "kwxymw") and (hwcri[-1] != "xgg")
xvbtl = Factor("uwmv", [DerivedLevel("duaqe", Transition(puj, [hwcri])), DerivedLevel("axiti", Transition(vtnkc, [hwcri])),DerivedLevel("cco", Transition(oohktt, [hwcri]))])
### EXPERIMENT
design=[hwcri,xvbtl]
crossing=[xvbtl]
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