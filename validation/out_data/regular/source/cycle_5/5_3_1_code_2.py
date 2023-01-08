from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qZiA_rdFb_ = Factor("qZiA&rdFb!", ["dhZz", "W]HTNkuTPPauH_", "dRSUOQN", "H?2cPcLFghVTlv", "O%aCsphHO", "@UfGUQ#oOE"])
BYbmeW_JhESi = Factor("BYbmeW]JhESi", ["Izhtx", "jd7mGapM", "0HVETiRa", "AZCw8vbYXO", " fdafalQj", "FLoZQfQEDLnC"])
F_GXAnimmff = Factor("F GXAnimmff", [Level("[VE", 1), Level("d:CFFaGGBtd", 3), Level("UeKS", 1), Level("lOs>ojr%eMbJ", 1), Level("1X1CnPsI>I1eeg", 1)])

design=[qZiA_rdFb_,BYbmeW_JhESi,F_GXAnimmff]
crossing=[qZiA_rdFb_,BYbmeW_JhESi,F_GXAnimmff]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_1"))

### END
