from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
dpgpee = Factor("dpgpee", ["griwc", "rcttpe"])
sbbw = Factor("sbbw", ["voq", "iatd"])
cbglx = Factor("cbglx", ["griwc", "rcttpe"])
kxru = Factor("kxru", ["voq", "iatd"])
design=[dpgpee,sbbw,cbglx,kxru]
constraints=[MinimumTrials(31)]
crossing=[cbglx,dpgpee]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_1"))
