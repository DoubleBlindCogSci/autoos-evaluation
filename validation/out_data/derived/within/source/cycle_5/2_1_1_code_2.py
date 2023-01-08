from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ifjkk = Factor("ifjkk", ["beov","mqkwty","pecsu","nnirya","opawtr","nqoiy","tnkurd"])
def is_fly_lqzlhe(ifjkk):
    return ifjkk == "tnkurd" and ifjkk != "pecsu"
def is_fly_orq(ifjkk):
    return not is_fly_lqzlhe(ifjkk)
fly = Factor("fly", [DerivedLevel("lqzlhe", WithinTrial(is_fly_lqzlhe, [ifjkk])), DerivedLevel("orq", WithinTrial(is_fly_orq, [ifjkk]))])

design=[ifjkk,fly]
crossing=[fly]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END