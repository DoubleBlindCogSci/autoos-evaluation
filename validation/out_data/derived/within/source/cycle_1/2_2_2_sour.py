from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
dkqkm = Factor("dkqkm", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
jmai = Factor("jmai", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
qtb = Factor("qtb", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
def ukpjvo(dkqkm, qtb, jmai):
    return dkqkm != qtb or dkqkm == jmai
def aphfj(dkqkm, qtb, jmai):
    return not (dkqkm != qtb) and dkqkm != jmai
hiv = DerivedLevel("rvgss", WithinTrial(ukpjvo, [dkqkm, jmai, qtb]))
wbdl = DerivedLevel("qdrcjx", WithinTrial(aphfj, [dkqkm, jmai, qtb]))
ehi = Factor("corru", [hiv, wbdl])

### EXPERIMENT
design=[dkqkm,jmai,qtb,ehi]
crossing=[ehi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)