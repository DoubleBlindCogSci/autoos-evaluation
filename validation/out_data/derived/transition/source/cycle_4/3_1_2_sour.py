from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hxtk = Factor("hxtk", ["rnl","umdg","xoc","bdfo","jood","iqjrov"])
def rlcndh(hxtk):
     return "iqjrov" == hxtk[0] and not hxtk[-1] == "jood"
def qldv(hxtk):
     return (not "iqjrov" != hxtk[0]) and  hxtk[-1] == "jood"
def zrnep(hxtk):
     return (not rlcndh(hxtk)) and (hxtk[-1] != "jood")
mgfvbg = DerivedLevel("xzyabw", Transition(rlcndh, [hxtk]))
zih = DerivedLevel("fqpfw", Transition(qldv, [hxtk]))
bimdrp = DerivedLevel("cacgyf", Transition(zrnep, [hxtk]))
ntpar = Factor("jofvzx", [mgfvbg, zih, bimdrp])

### EXPERIMENT
design=[hxtk,ntpar]
crossing=[ntpar]
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