from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
fihow = Factor("fihow", ["jppw", "ncs"])
xck = Factor("xck", ["tvtou", "ugknb"])
ezqy = Factor("ezqy", ["jppw", "ncs"])
hqwon = Factor("hqwon", ["tvtou", "ugknb"])
chs = Factor("chs", ["tlyj", "fbf"])
pxaz = Factor("pxaz", ["bfdnum", "nlo"])
constraints = [AtLeastKInARow(4, chs), AtMostKInARow(2, pxaz)]
crossing = [fihow, pxaz]

design=[fihow,xck,ezqy,hqwon,chs,pxaz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0_2"))
