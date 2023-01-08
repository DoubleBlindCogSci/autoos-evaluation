from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
zsin = Factor("zsin", ["keora", "obefln"])
zyf = Factor("zyf", ["vxcn", "vwxjol"])
psi = Factor("psi", ["keora", "obefln"])
tejntn = Factor("tejntn", ["vxcn", "vwxjol"])
hir = Factor("hir", ["hjsh", "aaba"])
design=[zsin,zyf,psi,tejntn,hir]
constraints=[]
crossing=[tejntn,hir]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_0"))
