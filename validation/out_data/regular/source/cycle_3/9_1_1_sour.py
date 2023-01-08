from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lmNbmTD=Factor("JKBPzBU",['U%FtEOSTpSwfjd','H~evAikoDEKVR',Level("ctredfO% CQ_",10),Level('X~SEnMhS',7),Level('icMpHODgz',8),"2UWYyW}(RJF#",Level("RwHxF?Ja",4),'Ke?lmHB2nnyNCT',"5xgSaZd>MXCxK"])

### EXPERIMENT
design=[lmNbmTD]
crossing=[lmNbmTD]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)