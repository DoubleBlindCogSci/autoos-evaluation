from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
bvtai = Factor("bvtai", ["pvuel", "slfm"])
lembv = Factor("lembv", ["wfibz", "tryd"])
tfo = Factor("tfo", ["pvuel", "slfm"])
jerk = Factor("jerk", ["wfibz", "tryd"])
design=[bvtai,lembv,tfo,jerk]
constraints=[MinimumTrials(58)]
crossing=[tfo,bvtai]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_1"))
