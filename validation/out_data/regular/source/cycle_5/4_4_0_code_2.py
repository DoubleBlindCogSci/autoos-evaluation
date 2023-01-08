from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KIjvFbXUcopz = Factor("KIjvFbXUcopz", ["pgsL", "ZPGskZAMaesama", "YB~)B!cDv>oQ^", "{tTJIa;", "ddspwc"])
SAmFY__UowhBKP = Factor("SAmFY^1UowhBKP", ["vEhWx$", "HIlrlr", "JvD", "}mO"])
soLnO = Factor("soLnO", [Level("qhCLBSMkJ;Dg5", 3), Level("1RPWRot>c", 1), Level("CK;1", 1), Level("SQl8zhw", 1), Level("NsRtrg", 1), Level("d:Wk3sEb^JZvYS", 1)])

design=[KIjvFbXUcopz,SAmFY__UowhBKP,soLnO]
crossing=[KIjvFbXUcopz,SAmFY__UowhBKP,soLnO]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_4_0"))

### END
