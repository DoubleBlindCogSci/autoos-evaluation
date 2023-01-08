from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dtx = Factor("dtx", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
wcftzr = Factor("wcftzr", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
jdewe = Factor("jdewe", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
def bxu(dtx, jdewe, wcftzr):
    return dtx != jdewe
def qkumf(dtx, jdewe, wcftzr):
    return dtx == jdewe
czdb = Factor("aumdnp", [DerivedLevel("gazr", WithinTrial(bxu, [dtx, wcftzr, jdewe])), DerivedLevel("kcn", WithinTrial(qkumf, [dtx, wcftzr, jdewe]))])
### EXPERIMENT
design=[dtx,wcftzr,jdewe,czdb]
crossing=[czdb]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)