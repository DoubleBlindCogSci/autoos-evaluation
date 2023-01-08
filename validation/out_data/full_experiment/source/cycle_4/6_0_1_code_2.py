from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
qgplsu = Factor("qgplsu", ["pboibu", "zqdel"])
jjssm = Factor("jjssm", ["riesgx", "mxl"])
xaqd = Factor("xaqd", ["pboibu", "zqdel"])
utkb = Factor("utkb", ["riesgx", "mxl"])
nsmo = Factor("nsmo", ["zaxwi", "zews"])
qpgyns = Factor("qpgyns", ["dha", "upj"])
constraints = [AtLeastKInARow(4, qpgyns)]
crossing = [qpgyns, nsmo]

design=[qgplsu,jjssm,xaqd,utkb,nsmo,qpgyns]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0_1"))
