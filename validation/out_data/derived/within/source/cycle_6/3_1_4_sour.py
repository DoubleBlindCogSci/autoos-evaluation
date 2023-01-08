from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tiypz = Factor("tiypz", ["hsbkic","qrfj","dlo","sclcq","jut","qbm","dcsj","hsiqw"])
def gjmmjy(tiypz):
     return "hsiqw" == tiypz
def ofuxkj(tiypz):
     return tiypz == "qbm"
def celxs(tiypz):
     return (not gjmmjy(tiypz)) and (not tiypz == "qbm")
zxiq = DerivedLevel("idqcya", WithinTrial(gjmmjy, [tiypz]))
knnlqr = DerivedLevel("fqw", WithinTrial(ofuxkj, [tiypz]))
qay = DerivedLevel("jnt", WithinTrial(celxs, [tiypz]))
bqg = Factor("dsujjh", [zxiq, knnlqr, qay])

### EXPERIMENT
design=[tiypz,bqg]
crossing=[bqg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)