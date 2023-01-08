from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gcM2dzT1S=Factor("kMXgAq",['RZzjWytRXBYKMC','gkk0TGK(GvI',"aAQXO_",Level('z!J}',2),"N6esUhr[6","hK{k7N",'TxGFPUBhBx',"vpulRruR|Kih",Level('l;riM',3)])

### EXPERIMENT
design=[gcM2dzT1S]
crossing=[gcM2dzT1S]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_1_0_0.csv"))
nr_factors=1
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)