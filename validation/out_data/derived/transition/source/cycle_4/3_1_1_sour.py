from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pzapf = Factor("pzapf", ["pac","nyn","nizn","ieem","qnrl","fpmsni","zdh"])
def ymiy(pzapf):
     return pzapf[0] == "fpmsni" and not pzapf[-1] == "ieem"
def mcmcr(pzapf):
     return (pzapf[0] != "fpmsni") and  pzapf[-1] == "ieem"
def vcv(pzapf):
     return (not ymiy(pzapf)) and (not mcmcr(pzapf))
sqrxnh = Factor("qrrz", [DerivedLevel("ehmlbs", Transition(ymiy, [pzapf])), DerivedLevel("aisbii", Transition(mcmcr, [pzapf])),DerivedLevel("irhh", Transition(vcv, [pzapf]))])
### EXPERIMENT
design=[pzapf,sqrxnh]
crossing=[sqrxnh]
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