from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
owxvgu = Factor("owxvgu", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
epixg = Factor("epixg", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
hwd = Factor("hwd", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
def gzmdl(owxvgu, epixg, hwd):
    return owxvgu[0] != epixg[-1]
def aquw(owxvgu, epixg, hwd):
    return not gzmdl(owxvgu, epixg, hwd)
xjt = DerivedLevel("akkuo", Transition(gzmdl, [owxvgu, epixg, hwd]))
znucw = DerivedLevel("gniz", Transition(aquw, [owxvgu, epixg, hwd]))
ubd = Factor("gxrai", [xjt, znucw])

### EXPERIMENT
design=[owxvgu,epixg,hwd,ubd]
crossing=[ubd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END