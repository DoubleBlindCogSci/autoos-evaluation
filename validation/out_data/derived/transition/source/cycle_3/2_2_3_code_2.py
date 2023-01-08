from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dqp = Factor("dqp", ["gxvwjg","ozlbks","may","ylvs","cto","zky"])
kvl = Factor("kvl", ["dnq","qni","gpep","dyaqc","kttnci","ytbknz"])
def is_mkdzgu_oodgw(dqp, kvl):
    return dqp[0] == "ylvs" and kvl[-1] != "kttnci"
def is_mkdzgu_sdvto(dqp, kvl):
    return not is_mkdzgu_oodgw(dqp, kvl)
mkdzgu= Factor("mkdzgu", [DerivedLevel("oodgw", Transition(is_mkdzgu_oodgw, [dqp, kvl])), DerivedLevel("sdvto", Transition(is_mkdzgu_sdvto, [dqp, kvl]))])

design=[dqp,kvl,mkdzgu]
crossing=[mkdzgu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
