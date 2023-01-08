from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zper = Factor("zper", ["flic","vdz","wek","ykwy","tvrztf","bwuwf","pmouuv"])
gjueol = Factor("gjueol", ["flic","vdz","wek","ykwy","tvrztf","bwuwf","pmouuv"])
folsmk = Factor("folsmk", ["flic","vdz","wek","ykwy","tvrztf","bwuwf","pmouuv"])
def is_lqi_qvi(zper, gjueol, folsmk):
    return zper[0] == gjueol[-1] and zper[-1] != folsmk[0]
def is_lqi_lqn(zper, gjueol, folsmk):
    return not is_lqi_qvi(zper, gjueol, folsmk)
lqi = Factor("lqi", [DerivedLevel("qvi", Transition(is_lqi_qvi, [zper, gjueol, folsmk])), DerivedLevel("lqn", Transition(is_lqi_lqn, [zper, gjueol, folsmk]))])

design=[zper,gjueol,folsmk,lqi]
crossing=[lqi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END