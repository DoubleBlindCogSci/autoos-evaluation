from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
swpbw = Factor("swpbw", ["gxqviy","kouncc","ywgbc","tellq","pglh","gbxc"])
def mnlull(swpbw):
     return "ywgbc" == swpbw
def kehvt(swpbw):
     return "kouncc" == swpbw
def wzkjew(swpbw):
     return (not swpbw == "ywgbc") and (swpbw != "kouncc")
bfmrt = DerivedLevel("cvw", WithinTrial(mnlull, [swpbw]))
slade = DerivedLevel("dbh", WithinTrial(kehvt, [swpbw]))
lzlvsz = DerivedLevel("ycnqcv", WithinTrial(wzkjew, [swpbw]))
qbugbq = Factor("xjf", [bfmrt, slade, lzlvsz])

### EXPERIMENT
design=[swpbw,qbugbq]
crossing=[qbugbq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END