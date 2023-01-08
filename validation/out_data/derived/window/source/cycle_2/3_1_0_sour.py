from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tdnox = Factor("tdnox", ["kqpv","hrotnx","dasrau","ybtjiu","hulttu","qacp"])
def wry(tdnox):
     return "hrotnx" == tdnox[-2] and not tdnox[-3] == "hrotnx"
def mwkbj(tdnox):
     return not "hrotnx" == tdnox[-2] and  "qacp" == tdnox[-3]
def nkyc(tdnox):
     return (not tdnox[-2] == "hrotnx") and (tdnox[-3] != "qacp")
xpon = Factor("tmvjq", [DerivedLevel("uto", Window(wry, [tdnox],4)), DerivedLevel("ifontz", Window(mwkbj, [tdnox],4)),DerivedLevel("ntqamr", Window(nkyc, [tdnox],4))])
### EXPERIMENT
design=[tdnox,xpon]
crossing=[xpon]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)