from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dNhiegChdNK=[Level("o20tcr",4),"E#K"]
JBBXBZ_Y=[dNhiegChdNK[0],"bkZgz[q:HF8hxt",Level('TRdM$5L',2),"nqlL?&XL",'rbvEa',Level("vqg",4),"7^QxENEOxB",'YeaGAaZv5M']
MzQCR3KEeh4=Factor("QpxkUz~vdhp",JBBXBZ_Y)

### EXPERIMENT
design=[MzQCR3KEeh4]
crossing=[MzQCR3KEeh4]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_1_1_0.csv"))
nr_factors=1
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)