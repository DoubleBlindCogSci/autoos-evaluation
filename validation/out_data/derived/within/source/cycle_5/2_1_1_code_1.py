from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ifjkk = Factor("ifjkk", ["beov","mqkwty","pecsu","nnirya","opawtr","nqoiy","tnkurd"])
def bvyrpp(ifjkk):
    return ifjkk == "tnkurd" and ifjkk != "pecsu"
def aqwn(ifjkk):
    return not (ifjkk == "tnkurd") or ifjkk == "pecsu"
aiztlu = DerivedLevel("lqzlhe", WithinTrial(bvyrpp, [ifjkk]))
ynqrsr = DerivedLevel("orq", WithinTrial(aqwn, [ifjkk]))
ecfy = Factor("fly", [aiztlu, ynqrsr])

### EXPERIMENT
design=[ifjkk,ecfy]
crossing=[ecfy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END