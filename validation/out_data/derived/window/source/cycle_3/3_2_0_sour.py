from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jfmjpo = Factor("jfmjpo", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
krk = Factor("krk", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
ktn = Factor("ktn", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
def jarw(jfmjpo, ktn, krk):
     return jfmjpo[-3] == ktn[-1] and jfmjpo[-1] != krk[-3]
def vweea(jfmjpo, ktn, krk):
     return ktn[-1] != jfmjpo[-3] and krk[-3] == jfmjpo[-1]
def jxve(jfmjpo, ktn, krk):
     return (not jarw(jfmjpo, ktn, krk)) and (not vweea(jfmjpo, ktn, krk))
elohps = Factor("faobo", [DerivedLevel("uqcsr", Window(jarw, [jfmjpo, krk, ktn],4)), DerivedLevel("nrzqy", Window(vweea, [jfmjpo, krk, ktn],4)),DerivedLevel("bzlj", Window(jxve, [jfmjpo, krk, ktn],4))])
### EXPERIMENT
design=[jfmjpo,krk,ktn,elohps]
crossing=[elohps]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)