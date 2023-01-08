from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gskuwm = Factor("gskuwm", ["qjoic", "ipvoln"])
ebmpb = Factor("ebmpb", ["bmb", "mlcydz"])
tnvcy = Factor("tnvcy", ["gvjh", "mqvfml"])
tdma = Factor("tdma", ["rhqfa", "qvrmrq"])
trwhbk = Factor("trwhbk", ["gltdhi", "gnu"])
dlzigb = Factor("dlzigb", ["vfxl", "chkyme"])
lpsmn = Factor("lpsmn", ["wbxok", "rawim"])
nucsu = Factor("nucsu", ["drktpc", "humuzy"])

### EXPERIMENT
design=[gskuwm,ebmpb,tnvcy,tdma,trwhbk,dlzigb,lpsmn,nucsu]
crossing=[[gskuwm,ebmpb],[tnvcy,tdma,trwhbk,dlzigb],[lpsmn,nucsu],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3"))
### END