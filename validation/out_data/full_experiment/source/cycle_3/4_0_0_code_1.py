from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
fgkj = Factor("fgkj", ["wuwwik", "ljlajb"])
yax = Factor("yax", ["ffv", "woyxmt"])
rfhpfx = Factor("rfhpfx", ["wuwwik", "ljlajb"])
wgxs = Factor("wgxs", ["ffv", "woyxmt"])
design=[fgkj,yax,rfhpfx,wgxs]
constraints=[]
crossing=[wgxs,yax]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_0"))
