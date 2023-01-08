from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cllom = Factor("cllom", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
dqbabm = Factor("dqbabm", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
hvd = Factor("hvd", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
def is_ucdmr_vcllmd(cllom, dqbabm, hvd):
    return dqbabm[-1] == cllom[0] and cllom[-1] != hvd[0]
def is_ucdmr_kvhw(cllom, dqbabm, hvd):
    return dqbabm[-1] != cllom[0] and cllom[-1] == hvd[0]
def is_ucdmr_zkoh(cllom, dqbabm, hvd):
    return not (is_ucdmr_vcllmd(cllom, dqbabm, hvd) or is_ucdmr_kvhw(cllom, dqbabm, hvd))
ucdmr= Factor("ucdmr", [DerivedLevel("vcllmd", Transition(is_ucdmr_vcllmd, [cllom, dqbabm, hvd])), DerivedLevel("kvhw", Transition(is_ucdmr_kvhw, [cllom, dqbabm, hvd])), DerivedLevel("zkoh", Transition(is_ucdmr_zkoh, [cllom, dqbabm, hvd]))])

design=[cllom,dqbabm,hvd,ucdmr]
crossing=[ucdmr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END