from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NqAFPs_=Factor("e]BLDhPJxxVlKg",[Level("rVFK%efrn(",2),'ewKxWHKQ4Caj0z',"6FSwnPmY9n9bq#",'tVCTaPadT9LRx',"lchXR|IVJnNI@H","ds5PpnziIV",'h*iogeZ'])
igDLECsfHcE=['lmCt^X','n@km','c>Du{','GfZj@ECU','%YhNi',"qdq5HD3RKd",Level("HsDC^k(VGqH)A",3)]
NwBBt31qTk=Factor('XPW4bGN?BG',igDLECsfHcE)
LlpgFL=Factor('Fhp#T]E',['hWa<',"lLq2i",Level("DygoWtyh<T",9),'AuKb^ktTOq',"enj_FFt",'Ez7Y',"nX@IShbxrHhtr"])

### EXPERIMENT
design=[NqAFPs_,NwBBt31qTk,LlpgFL]
crossing=[NqAFPs_,NwBBt31qTk,LlpgFL]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_3_1_0.csv"))
nr_factors=3
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)