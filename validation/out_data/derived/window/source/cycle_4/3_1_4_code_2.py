from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
miyzdq = Factor("miyzdq", ["klaaay","qyw","vmzbe","jzywnf","kklavl","aalk","zyek","dtpi"])
def is_brsv_animf(miyzdq):
    return miyzdq[-2] == "klaaay" and miyzdq[0] != "klaaay"
def is_brsv_dpmihp(miyzdq):
    return miyzdq[-2] != "klaaay" and miyzdq[0] == "aalk"
def is_brsv_ypsd(miyzdq):
    return not (is_brsv_animf(miyzdq) or is_brsv_dpmihp(miyzdq))
brsv = Factor("brsv", [DerivedLevel("animf", Window(is_brsv_animf, [miyzdq], 3, 1)), DerivedLevel("dpmihp", Window(is_brsv_dpmihp, [miyzdq], 3, 1)), DerivedLevel("ypsd", Window(is_brsv_ypsd, [miyzdq], 3, 1))])

design=[miyzdq,brsv]
crossing=[brsv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END