from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
owxvgu = Factor("owxvgu", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
epixg = Factor("epixg", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
hwd = Factor("hwd", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
def is_gxrai_akkuo(owxvgu, epixg, hwd):
    return owxvgu[0] != epixg[-1]
def is_gxrai_gniz(owxvgu, epixg, hwd):
    return not is_gxrai_akkuo(owxvgu, epixg, hwd)
gxrai = Factor("gxrai", [DerivedLevel("akkuo", Transition(is_gxrai_akkuo, [owxvgu, epixg, hwd])), DerivedLevel("gniz", Transition(is_gxrai_gniz, [owxvgu, epixg, hwd]))])

design=[owxvgu,epixg,hwd,gxrai]
crossing=[gxrai]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END