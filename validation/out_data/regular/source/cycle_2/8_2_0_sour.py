from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ocvb=Factor("6nMFHmg",['U RPg',Level('U>eAy',9),Level('nMBLBD',6),'TFPr7Azswr','deEUu',"hqp",'%ZoTnVTIe&',"M:z]GH"])
gg0KkMEO4=[Level('lqAK4QobG_zBVR',2),Level("isRd",5),Level("PNm",2),'BMMmNTpyMD','}dzpC8',"i$Nm",Level("BMPhQNUw",8),"DGIUu}"]
YD_3=Factor('RryaCHD<QG',gg0KkMEO4)

### EXPERIMENT
design=[Ocvb,YD_3]
crossing=[Ocvb,YD_3]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_0_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)