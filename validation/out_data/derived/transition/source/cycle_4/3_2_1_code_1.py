from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cllom = Factor("cllom", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
dqbabm = Factor("dqbabm", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
hvd = Factor("hvd", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
def tar(cllom, dqbabm, hvd):
     return dqbabm[-1] == cllom[0] and cllom[-1] != hvd[0]
def ngmexx(cllom, dqbabm, hvd):
     return dqbabm[-1] != cllom[0] and cllom[-1] == hvd[0]
def qke(cllom, dqbabm, hvd):
     return (cllom[0] != dqbabm[-1]) and (cllom[-1] != hvd[0])
yreign = DerivedLevel("vcllmd", Transition(tar, [cllom, dqbabm, hvd]))
gtbv = DerivedLevel("kvhw", Transition(ngmexx, [cllom, dqbabm, hvd]))
irnehw = DerivedLevel("zkoh", Transition(qke, [cllom, dqbabm, hvd]))
mecohz = Factor("ucdmr", [yreign, gtbv, irnehw])

### EXPERIMENT
design=[cllom,dqbabm,hvd,mecohz]
crossing=[mecohz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END