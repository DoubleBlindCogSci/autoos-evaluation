from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
bvtai = Factor("bvtai", ["pvuel", "slfm"])
lembv = Factor("lembv", ["wfibz", "tryd"])
tfo = Factor("tfo", ["pvuel", "slfm"])
jerk = Factor("jerk", ["wfibz", "tryd"])
constraints = [MinimumTrials(58)]
crossing = [tfo, bvtai]

design=[bvtai,lembv,tfo,jerk]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_1"))
