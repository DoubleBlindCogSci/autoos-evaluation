from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
biu = Factor("biu", ["sassd","gotujg","elrdw","umju","kdzoug"])
fva = Factor("fva", ["sassd","gotujg","elrdw","umju","kdzoug"])
xpdbm = Factor("xpdbm", ["sassd","gotujg","elrdw","umju","kdzoug"])
def lgusp(biu, xpdbm, fva):
    return biu != xpdbm and biu == fva
def ekz(biu, xpdbm, fva):
    return not lgusp(biu, xpdbm, fva)
tftezd = Factor("zaab", [DerivedLevel("btyx", WithinTrial(lgusp, [biu, fva, xpdbm])), DerivedLevel("mbxq", WithinTrial(ekz, [biu, fva, xpdbm]))])
### EXPERIMENT
design=[biu,fva,xpdbm,tftezd]
crossing=[tftezd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)