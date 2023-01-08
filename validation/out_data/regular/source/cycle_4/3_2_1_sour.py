from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BiXDXCLlL=Factor(")xywqJoUzh",["NuE2","WAt",Level('W66ltFgIjag',4)])
BSsCidLJ6=Factor("?brQB",['SzcCqu(]SLL8',Level('NVW(',4),'(@kYc'])

### EXPERIMENT
design=[BiXDXCLlL,BSsCidLJ6]
crossing=[BiXDXCLlL,BSsCidLJ6]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_factors=2
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)