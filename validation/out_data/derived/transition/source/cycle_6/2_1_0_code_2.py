from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fgmlne = Factor("fgmlne", ["pnacnl","madj","atiitg","hlt","ukkn","okdc"])
def is_mrun_yfnrep(fgmlne):
    return fgmlne[0] != "okdc" or fgmlne[-1] == "pnacnl"
def is_mrun_bxvkh(fgmlne):
    return not is_mrun_yfnrep(fgmlne)
mrun = Factor("mrun", [DerivedLevel("yfnrep", Transition(is_mrun_yfnrep, [fgmlne])), DerivedLevel("bxvkh", Transition(is_mrun_bxvkh, [fgmlne]))])

design=[fgmlne,mrun]
crossing=[mrun]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END