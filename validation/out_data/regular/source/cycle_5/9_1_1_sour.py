from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Snvb=Factor("cmEc[JU2p",["c9QZvI^rfrKM",'VroUQ(Ys',"Bt0Z","nEQVMmO",Level('YNvvFVv',2),'U(CegASjt&',Level("KMgp$",1),"iAKYajm uRQ%X",Level('|BrrihbKua~',3)])

### EXPERIMENT
design=[Snvb]
crossing=[Snvb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_1_1_0.csv"))
nr_factors=1
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)