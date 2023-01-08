from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ldl = Factor("ldl", ["xtgz","acrbvr","jkvqrs","bsmf","ten","ecs"])
def hwmyr(ldl):
    return ldl[-1] != "xtgz" and ldl[0] != "ecs"
def pcjf(ldl):
    return ldl[-1] == "xtgz" or not (ldl[0] != "ecs")
wwfqv = DerivedLevel("roopgk", Window(hwmyr, [ldl],2,1))
cchhqp = DerivedLevel("ehauj", Window(pcjf, [ldl],2,1))
lqxls = Factor("gwyg", [wwfqv, cchhqp])

### EXPERIMENT
design=[ldl,lqxls]
crossing=[lqxls]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END