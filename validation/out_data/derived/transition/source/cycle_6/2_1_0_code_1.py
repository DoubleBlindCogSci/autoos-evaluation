from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fgmlne = Factor("fgmlne", ["pnacnl","madj","atiitg","hlt","ukkn","okdc"])
def qrobob(fgmlne):
    return fgmlne[0] != "okdc" or fgmlne[-1] == "pnacnl"
def lrqnj(fgmlne):
    return not qrobob(fgmlne)
vlkw = DerivedLevel("yfnrep", Transition(qrobob, [fgmlne]))
txy = DerivedLevel("bxvkh", Transition(lrqnj, [fgmlne]))
krecn = Factor("mrun", [vlkw, txy])

### EXPERIMENT
design=[fgmlne,krecn]
crossing=[krecn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END