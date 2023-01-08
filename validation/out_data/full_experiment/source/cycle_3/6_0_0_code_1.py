from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
jjqf = Factor("jjqf", ["bxq", "jzroyg"])
vvwpqv = Factor("vvwpqv", ["ohm", "vkso"])
cohk = Factor("cohk", ["bxq", "jzroyg"])
cnicb = Factor("cnicb", ["ohm", "vkso"])
jov = Factor("jov", ["pqbif", "cvhpss"])
jxz = Factor("jxz", ["zdl", "cozev"])
design=[jjqf,vvwpqv,cohk,cnicb,jov,jxz]
constraints=[]
crossing=[cohk,vvwpqv]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_0_0"))
