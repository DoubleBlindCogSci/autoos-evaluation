from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dqp = Factor("dqp", ["gxvwjg","ozlbks","may","ylvs","cto","zky"])
kvl = Factor("kvl", ["dnq","qni","gpep","dyaqc","kttnci","ytbknz"])
def rtdy(dqp, kvl):
    return dqp[0] == "ylvs" and kvl[-1] != "kttnci"
def hjilgk(dqp,kvl):
    return not rtdy(dqp, kvl)
egfl = Factor("mkdzgu", [DerivedLevel("oodgw", Transition(rtdy, [dqp, kvl])), DerivedLevel("sdvto", Transition(hjilgk, [dqp, kvl]))])
### EXPERIMENT
design=[dqp,kvl,egfl]
crossing=[egfl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END