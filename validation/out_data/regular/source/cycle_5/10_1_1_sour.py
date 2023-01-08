from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xuA1iTJs0=Factor("@tlmBMqKyTQpk",['LSk','aU{y>>Kz','5AK',"ggttkmK5gLyw",'?YDNXax@P','sjDZylk',"6goF",Level('y1IloF:khMSw5T',2),"ZofSvJE8p",'6|UdTVw'])

### EXPERIMENT
design=[xuA1iTJs0]
crossing=[xuA1iTJs0]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/10_1_1_0.csv"))
nr_factors=1
nr_levels=10
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/10_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)