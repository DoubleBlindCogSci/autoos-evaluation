from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
abxksw = Factor("abxksw", ["wzgzq", "emk"])
sgv = Factor("sgv", ["waqco", "hcjxuf"])
felonu = Factor("felonu", ["wzgzq", "emk"])
zwt = Factor("zwt", ["waqco", "hcjxuf"])
constraints = []
crossing = [abxksw, felonu]

design=[abxksw,sgv,felonu,zwt]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_0"))
