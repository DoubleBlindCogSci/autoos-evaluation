from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ldl = Factor("ldl", ["xtgz","acrbvr","jkvqrs","bsmf","ten","ecs"])
def hwmyr(ldl):
    return ldl[-1] != "xtgz" and ldl[0] != "ecs"
def pcjf(ldl):
    return ldl[-1] == "xtgz" or not (ldl[0] != "ecs")
wwfqv = DerivedLevel("roopgk", Window(hwmyr, [ldl],2))
cchhqp = DerivedLevel("ehauj", Window(pcjf, [ldl],2))
lqxls = Factor("gwyg", [wwfqv, cchhqp])

### EXPERIMENT
design=[ldl,lqxls]
crossing=[lqxls]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)