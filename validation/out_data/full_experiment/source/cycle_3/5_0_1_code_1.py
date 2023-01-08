from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
hzss = Factor("hzss", ["ujnts", "jkw"])
kdzg = Factor("kdzg", ["xdrmxs", "asdgvm"])
axn = Factor("axn", ["ujnts", "jkw"])
cvf = Factor("cvf", ["xdrmxs", "asdgvm"])
djjd = Factor("djjd", ["vymblj", "sii"])
design=[hzss,kdzg,axn,cvf,djjd]
constraints=[AtLeastKInARow(4, axn)]
crossing=[cvf,hzss]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_1"))
