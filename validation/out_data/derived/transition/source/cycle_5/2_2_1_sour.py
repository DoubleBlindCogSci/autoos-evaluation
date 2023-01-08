from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rnmqww = Factor("rnmqww", ["jas","drhz","jglx","deji","jqshvt","zktr","mhm"])
vhln = Factor("vhln", ["adqrok","yha","bij","jeilkw","iamwb"])
def jrh(rnmqww, vhln):
    return rnmqww[0] == "jas" and vhln[-1] != "jeilkw"
def puelhm(rnmqww,vhln):
    return rnmqww[0] != "jas" or vhln[-1] == "jeilkw"
zjjkpw = DerivedLevel("xiarzr", Transition(jrh, [rnmqww, vhln]))
kjzh = DerivedLevel("mmf", Transition(puelhm, [rnmqww, vhln]))
phf = Factor("qgpn", [zjjkpw, kjzh])

### EXPERIMENT
design=[rnmqww,vhln,phf]
crossing=[phf]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)