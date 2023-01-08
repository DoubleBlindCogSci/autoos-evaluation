from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qoff = Factor("qoff", ["khzrnt","ctl","epkxxn","eirwnx","hwc"])
def hwop(qoff):
    return qoff[-1] == "hwc" or qoff[-2] == "epkxxn"
def wburc(qoff):
    return qoff[-1] != "hwc" and not (qoff[-2] == "epkxxn")
vex = Factor("krgdwu", [DerivedLevel("ghtrxk", Window(hwop, [qoff],3,1)), DerivedLevel("vmrh", Window(wburc, [qoff],3,1))])
### EXPERIMENT
design=[qoff,vex]
crossing=[vex]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END