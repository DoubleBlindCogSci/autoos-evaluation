from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ebrckx = Factor("ebrckx", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
qfzure = Factor("qfzure", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
jgvfzo = Factor("jgvfzo", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
def uwxtd(ebrckx, jgvfzo, qfzure):
     return jgvfzo[-1] == ebrckx[0] and ebrckx[-1] != qfzure[0]
def xtvd(ebrckx, jgvfzo, qfzure):
     return jgvfzo[-1] != ebrckx[0] and ebrckx[-1] == qfzure[0]
def ywuhoz(ebrckx, jgvfzo, qfzure):
     return (not uwxtd(ebrckx, jgvfzo, qfzure)) and (not ebrckx[-1] == qfzure[0])
rhpm = DerivedLevel("bahnt", Transition(uwxtd, [ebrckx, qfzure, jgvfzo]))
iye = DerivedLevel("ezdu", Transition(xtvd, [ebrckx, qfzure, jgvfzo]))
hgccu = DerivedLevel("atwd", Transition(ywuhoz, [ebrckx, qfzure, jgvfzo]))
yvdgi = Factor("lfako", [rhpm, iye, hgccu])

### EXPERIMENT
design=[ebrckx,qfzure,jgvfzo,yvdgi]
crossing=[yvdgi]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)