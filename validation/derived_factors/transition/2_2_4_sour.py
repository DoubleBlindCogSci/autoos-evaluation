from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uxje = Factor("uxje", ["hikpm","bgzcrc","zgt","xcjs","jiy","ptmx"])
drz = Factor("drz", ["hikpm","bgzcrc","zgt","xcjs","jiy","ptmx"])
cpvt = Factor("cpvt", ["hikpm","bgzcrc","zgt","xcjs","jiy","ptmx"])
def jirbjm(uxje, drz, cpvt):
    return uxje[0] == drz[-1] and uxje[-1] == cpvt[0]
def giic(uxje, drz, cpvt):
    return not (uxje[0] == drz[-1]) or uxje[-1] != cpvt[0]
hbmke = DerivedLevel("uke", Transition(jirbjm, [uxje, drz, cpvt]))
gehxc = DerivedLevel("dojeo", Transition(giic, [uxje, drz, cpvt]))
azwc = Factor("hft", [hbmke, gehxc])

### EXPERIMENT
design=[uxje,drz,cpvt,azwc]
crossing=[azwc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)