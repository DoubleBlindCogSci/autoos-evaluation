from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GseqZ=Level('t<AO?',5)
hdyYOJu='w9hLF?giSBh)'
Sj3GTvL3=Factor("jGeqqZm}fQLd",[Level('wTs5?jadFEQ',4),GseqZ,hdyYOJu,'IOl~bYjzwl','jvk3r;CcHD',"LzSqYRTdVFkz",'G8bJWpRd?'])

### EXPERIMENT
design=[Sj3GTvL3]
crossing=[Sj3GTvL3]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_1_0.csv"))
nr_factors=1
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)