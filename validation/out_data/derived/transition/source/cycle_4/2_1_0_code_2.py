from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gkonmr = Factor("gkonmr", ["feeesy","tojkq","rku","bkf","hcpsb","nzov","kgusl"])
def is_ove_jcsjia(gkonmr):
    return gkonmr[0] == "feeesy" or gkonmr[-1] == "rku"
def is_ove_iglkje(gkonmr):
    return not is_ove_jcsjia(gkonmr)
ove= Factor("ove", [DerivedLevel("jcsjia", Transition(is_ove_jcsjia, [gkonmr])), DerivedLevel("iglkje", Transition(is_ove_iglkje, [gkonmr]))])

design=[gkonmr,ove]
crossing=[ove]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END