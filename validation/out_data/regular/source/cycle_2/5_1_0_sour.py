from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
C9vdKnAkLY=[Level("VzUCehpBnaP",3),Level('uDBGgsjDf2Q',1),Level("vTxdbNj",9),"ua9E} f",Level("1tGp2tK",5)]
Z7oaO=Factor("JarEPo",C9vdKnAkLY)

### EXPERIMENT
design=[Z7oaO]
crossing=[Z7oaO]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_0_0.csv"))
nr_factors=1
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)