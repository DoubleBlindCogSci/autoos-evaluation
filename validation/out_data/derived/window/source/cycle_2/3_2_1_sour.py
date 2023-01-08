from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
eqhxp = Factor("eqhxp", ["oaylp","uisvq","mvc","trrtn","etz","vvixp"])
fkxb = Factor("fkxb", ["zqthl","eoxhfp","nipkq","fvud","sxndfe","teif","lzeks","brcsus"])
def umiy(eqhxp, fkxb):
     return "etz" == eqhxp[0] and fkxb[-1] != "teif"
def ptui(eqhxp, fkxb):
     return "etz" != eqhxp[0] and  fkxb[-1] == "teif"
def kvvy(eqhxp, fkxb):
     return (eqhxp[0] != "etz") and (fkxb[-1] != "teif")
lzoz = DerivedLevel("tmu", Window(umiy, [eqhxp, fkxb],2))
shykef = DerivedLevel("qdhzdb", Window(ptui, [eqhxp, fkxb],2))
hyrw = DerivedLevel("qkejh", Window(kvvy, [eqhxp, fkxb],2))
pvbnd = Factor("url", [lzoz, shykef, hyrw])

### EXPERIMENT
design=[eqhxp,fkxb,pvbnd]
crossing=[pvbnd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)