from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zper = Factor("zper", ["flic","vdz","wek","ykwy","tvrztf","bwuwf","pmouuv"])
gjueol = Factor("gjueol", ["flic","vdz","wek","ykwy","tvrztf","bwuwf","pmouuv"])
folsmk = Factor("folsmk", ["flic","vdz","wek","ykwy","tvrztf","bwuwf","pmouuv"])
def lvtp(zper, gjueol, folsmk):
    return zper[0] == gjueol[-1] and zper[-1] != folsmk[0]
def enjsp(zper, gjueol, folsmk):
    return not lvtp(zper, gjueol, folsmk)
oauu = DerivedLevel("qvi", Transition(lvtp, [zper, gjueol, folsmk]))
vklvy = DerivedLevel("lqn", Transition(enjsp, [zper, gjueol, folsmk]))
qhhnid = Factor("lqi", [oauu, vklvy])

### EXPERIMENT
design=[zper,gjueol,folsmk,qhhnid]
crossing=[qhhnid]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END