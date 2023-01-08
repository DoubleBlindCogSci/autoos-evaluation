from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
A28tvrBRF4=Factor("ufcU",["n *CPd",Level('A1x %OydT',10),Level("uIZZirH!kEYwIg",7),Level('PIJGKRCnawR',5),Level('(MatxpxIQo',9),'UzD',"nf9cvX"])
N9vI1yEBhS3=[Level("*BFnz",2),'wHtvDBrYsxy',";kFWwrleT",Level('ABvq:YM^kO',7),'1UROfWtA|HTbk',Level('RthmVAcUJ%u]RT',1),'ctS']
sjkyy=Factor('QG ',N9vI1yEBhS3)

### EXPERIMENT
design=[A28tvrBRF4,sjkyy]
crossing=[A28tvrBRF4,sjkyy]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_1_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)