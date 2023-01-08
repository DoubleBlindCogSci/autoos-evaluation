from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rbem= Factor("rbem", ["zerp","pqyoqq","uzz","znwo","fzahge","uukrt","oqiqce"])
def is_efpet_bzh(rbem):
    return rbem[0] == rbem[-1]
def is_efpet_edv(rbem):
    return rbem[0] == rbem[-3]
def is_efpet_ymqe(rbem):
    return not (is_efpet_bzh(rbem) or is_efpet_edv(rbem))
efpet= Factor("efpet", [DerivedLevel("bzh", Window(is_efpet_bzh, [rbem], 4, 1)), DerivedLevel("edv", Window(is_efpet_edv, [rbem], 4, 1)), DerivedLevel("ymqe", Window(is_efpet_ymqe, [rbem], 4, 1))])

design=[rbem,efpet]
crossing=[efpet]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
