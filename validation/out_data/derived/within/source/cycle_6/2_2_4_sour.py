from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
lovf = Factor("lovf", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
prpbhg = Factor("prpbhg", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
rnik = Factor("rnik", ["adie","qlvciq","cudczl","jrr","kovp","xmntrp","hthrc"])
def zyb(lovf, rnik, prpbhg):
    return lovf == rnik
def ytaig(lovf, rnik, prpbhg):
    return lovf != rnik
jibma = DerivedLevel("ldor", WithinTrial(zyb, [lovf, prpbhg, rnik]))
womtv = DerivedLevel("rue", WithinTrial(ytaig, [lovf, prpbhg, rnik]))
exrux = Factor("fuvcg", [jibma, womtv])

### EXPERIMENT
design=[lovf,prpbhg,rnik,exrux]
crossing=[exrux]
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