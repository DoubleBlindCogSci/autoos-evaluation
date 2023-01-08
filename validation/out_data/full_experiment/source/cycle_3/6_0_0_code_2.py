from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
jjqf = Factor("jjqf", ["bxq", "jzroyg"])
vvwpqv = Factor("vvwpqv", ["ohm", "vkso"])
cohk = Factor("cohk", ["bxq", "jzroyg"])
cnicb = Factor("cnicb", ["ohm", "vkso"])
jov = Factor("jov", ["pqbif", "cvhpss"])
jxz = Factor("jxz", ["zdl", "cozev"])
constraints = []
crossing = [cohk, vvwpqv]

design=[jjqf,vvwpqv,cohk,cnicb,jov,jxz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0_0"))
