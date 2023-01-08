from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ubgs = Factor("ubgs", ["tddsj", "pru"])
htydch = Factor("htydch", ["lsqmxp", "xuukpx"])
tclwi = Factor("tclwi", ["tddsj", "pru"])
kvxse = Factor("kvxse", ["lsqmxp", "xuukpx"])
icb = Factor("icb", ["qsc", "fjil"])
rfsofe = Factor("rfsofe", ["zcu", "gzr"])
design=[ubgs,htydch,tclwi,kvxse,icb,rfsofe]
constraints=[]
crossing=[kvxse,icb]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_0_0"))
