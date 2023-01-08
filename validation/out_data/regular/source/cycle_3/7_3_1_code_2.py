from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
e_BLDhPJxxVlKg = Factor("e]BLDhPJxxVlKg", [Level("rVFK%efrn(", 2), "ewKxWHKQ4Caj0z", "6FSwnPmY9n9bq#", "tVCTaPadT9LRx", "lchXR|IVJnNI@H", "ds5PpnziIV", "h*iogeZ"])
XPW_bGN_BG = Factor("XPW4bGN?BG", ["lmCt^X", "@km", "c>Du{", "GfZj@ECU", "%YhNi", "qdq5HD3RKd", Level("HsDC^k(VGqH)A", 3)])
Fhp_T_E = Factor("Fhp#T]E", ["hWa<", "lLq2i", Level("DygoWtyh<T", 9), "AuKb^ktTOq", "enj_FFt", "Ez7Y", "nX@IShbxrHhtr"])

design=[e_BLDhPJxxVlKg,XPW_bGN_BG,Fhp_T_E]
crossing=[e_BLDhPJxxVlKg,XPW_bGN_BG,Fhp_T_E]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_1"))

### END
