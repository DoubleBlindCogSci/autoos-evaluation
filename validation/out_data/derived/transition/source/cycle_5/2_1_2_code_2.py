from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bbjw = Factor("bbjw", ["xij","bjijfm","wuglr","wtgr","emktn","sqnz"])
def is_hklsq_ehyzcl(bbjw):
    return bbjw[0] == "wuglr" or bbjw[-1] != "xij"
def is_hklsq_axrv(bbjw):
    return not is_hklsq_ehyzcl(bbjw)
hklsq = Factor("hklsq", [DerivedLevel("ehyzcl", Transition(is_hklsq_ehyzcl, [bbjw])), DerivedLevel("axrv", Transition(is_hklsq_axrv, [bbjw]))])

design=[bbjw,hklsq]
crossing=[hklsq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END