from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
djaod = Factor("djaod", ["mheqs","aewzew","pokcw","jlr","xvdbtl","qednx","job"])
moccj = Factor("moccj", ["awupod","zuyzk","butf","ybg","aywgfe"])
def akrw(djaod, moccj):
    return djaod[-1] != "xvdbtl" and moccj[0] == "aywgfe"
def mjoo(djaod,moccj):
    return not (djaod[-1] != "xvdbtl") or moccj[0] != "aywgfe"
kewu = DerivedLevel("ocebmw", Window(akrw, [djaod, moccj],2))
dgp = DerivedLevel("ysotd", Window(mjoo, [djaod, moccj],2))
wsah = Factor("rcxfsi", [kewu, dgp])

### EXPERIMENT
design=[djaod,moccj,wsah]
crossing=[wsah]
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