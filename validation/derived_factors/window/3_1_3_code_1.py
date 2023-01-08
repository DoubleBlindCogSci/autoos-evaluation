from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
farry = Factor("farry", ["xaagha","xsa","vsalcr","gxzv","zormi","twt"])
def wll(farry):
     return farry[0] == "vsalcr" and not farry[-2] == "vsalcr"
def ndxzt(farry):
     return not "vsalcr" == farry[0] and  farry[-2] == "zormi"
def gxhvm(farry):
     return (farry[0] != "vsalcr") and (not farry[-2] == "zormi")
udfe = Factor("cnlsvq", [DerivedLevel("aykqdz", Window(wll, [farry],3,1)), DerivedLevel("jvkuru", Window(ndxzt, [farry],3,1)),DerivedLevel("vxfzd", Window(gxhvm, [farry],3,1))])
### EXPERIMENT
design=[farry,udfe]
crossing=[udfe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END