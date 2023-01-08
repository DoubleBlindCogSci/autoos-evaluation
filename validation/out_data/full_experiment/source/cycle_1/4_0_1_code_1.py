from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
xti = Factor("xti", ["hdlc", "nodrfn"])
nzuufr = Factor("nzuufr", ["bev", "vbequ"])
bxk = Factor("bxk", ["hdlc", "nodrfn"])
gokv = Factor("gokv", ["bev", "vbequ"])
design=[xti,nzuufr,bxk,gokv]
constraints=[AtMostKInARow(2, nzuufr)]
crossing=[gokv,nzuufr]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_0_1"))
