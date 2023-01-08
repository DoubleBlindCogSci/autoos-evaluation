from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
unrxx = Factor("unrxx", ["juabnh", "gbnqm"])
vvdgwd = Factor("vvdgwd", ["ccwoqj", "zevijt"])
fbr = Factor("fbr", ["juabnh", "gbnqm"])
fqyzr = Factor("fqyzr", ["ccwoqj", "zevijt"])
qqgqvy = Factor("qqgqvy", ["jmterk", "ripcij"])
design=[unrxx,vvdgwd,fbr,fqyzr,qqgqvy]
constraints=[AtLeastKInARow(4, qqgqvy)]
crossing=[unrxx,fbr]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_0_1"))
