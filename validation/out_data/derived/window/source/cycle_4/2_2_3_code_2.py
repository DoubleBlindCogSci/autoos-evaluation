from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ouggqp = Factor("ouggqp", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
eylw = Factor("eylw", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
iji = Factor("iji", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
def is_orl_jteux(ouggqp, eylw, iji):
    return ouggqp[0] == eylw[-2]
def is_orl_oknyrj(ouggqp, eylw, iji):
    return not is_orl_jteux(ouggqp, eylw, iji)
orl = Factor("orl", [DerivedLevel("jteux", Window(is_orl_jteux, [ouggqp, eylw, iji], 3, 1)), DerivedLevel("oknyrj", Window(is_orl_oknyrj, [ouggqp, eylw, iji], 3, 1))])

design=[ouggqp,eylw,iji,orl]
crossing=[orl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END