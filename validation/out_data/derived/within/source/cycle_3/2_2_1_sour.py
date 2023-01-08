from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bhlc = Factor("bhlc", ["ytqhf","rma","ilbt","aiyuj","pwo","jno","rxrnp"])
jqwma = Factor("jqwma", ["tmc","elrer","tezuge","xbkz","imbn"])
def ezz(bhlc, jqwma):
    return bhlc != "ilbt" or jqwma == "tezuge"
def bjanw(bhlc,jqwma):
    return not ezz(bhlc, jqwma)
rmedy = DerivedLevel("ecbu", WithinTrial(ezz, [bhlc, jqwma]))
hnkvbp = DerivedLevel("lugj", WithinTrial(bjanw, [bhlc, jqwma]))
fpvufl = Factor("yva", [rmedy, hnkvbp])

### EXPERIMENT
design=[bhlc,jqwma,fpvufl]
crossing=[fpvufl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)