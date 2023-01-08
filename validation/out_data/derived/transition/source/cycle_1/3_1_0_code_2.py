from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iraw= Factor("iraw", ["uyv","aiyucw","ofd","yrk","nhzpt","incd"])
def is_goetv_luve(iraw):
    return iraw[0] == "ofd"
def is_goetv_wxp(iraw):
    return iraw[0] == "uyv"
def is_goetv_zjqnkh(iraw):
    return not (is_goetv_luve(iraw) or is_goetv_wxp(iraw))
goetv= Factor("goetv", [DerivedLevel("luve", Transition(is_goetv_luve, [iraw])), DerivedLevel("wxp", Transition(is_goetv_wxp, [iraw])), DerivedLevel("zjqnkh", Transition(is_goetv_zjqnkh, [iraw]))])

design=[iraw,goetv]
crossing=[goetv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
