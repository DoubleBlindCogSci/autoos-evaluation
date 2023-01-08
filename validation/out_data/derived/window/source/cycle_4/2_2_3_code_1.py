from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ouggqp = Factor("ouggqp", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
eylw = Factor("eylw", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
iji = Factor("iji", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
def cbhf(ouggqp, eylw, iji):
    return ouggqp[0] == eylw[-2]
def ugb(ouggqp, eylw, iji):
    return not cbhf(ouggqp, eylw, iji)
gsgqmk = DerivedLevel("jteux", Window(cbhf, [ouggqp, eylw, iji],3,1))
lsom = DerivedLevel("oknyrj", Window(ugb, [ouggqp, eylw, iji],3,1))
vapd = Factor("orl", [gsgqmk, lsom])

### EXPERIMENT
design=[ouggqp,eylw,iji,vapd]
crossing=[vapd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END