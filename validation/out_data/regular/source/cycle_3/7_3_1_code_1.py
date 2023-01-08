from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_1"))
### END