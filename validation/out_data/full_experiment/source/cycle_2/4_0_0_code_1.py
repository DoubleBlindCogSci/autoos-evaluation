from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
abxksw = Factor("abxksw", ["wzgzq", "emk"])
sgv = Factor("sgv", ["waqco", "hcjxuf"])
felonu = Factor("felonu", ["wzgzq", "emk"])
zwt = Factor("zwt", ["waqco", "hcjxuf"])
design=[abxksw,sgv,felonu,zwt]
constraints=[]
crossing=[abxksw,felonu]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_0"))
