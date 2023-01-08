from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xegutz = Factor("xegutz", ["qzsw","fzvbw","xda","jdmilo","gaalwi","bdmqeu"])
wmxmym = Factor("wmxmym", ["lrwzfp","ysr","qjnpiy","azaopl","use","evg","ppqz"])
def wprj(xegutz, wmxmym):
    return xegutz != "bdmqeu" and wmxmym != "ppqz"
def mbujl(xegutz,wmxmym):
    return xegutz == "bdmqeu" or wmxmym == "ppqz"
zbwucb = DerivedLevel("hhir", WithinTrial(wprj, [xegutz, wmxmym]))
qhepcp = DerivedLevel("ebhy", WithinTrial(mbujl, [xegutz, wmxmym]))
jqocq = Factor("dln", [zbwucb, qhepcp])

### EXPERIMENT
design=[xegutz,wmxmym,jqocq]
crossing=[jqocq]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)