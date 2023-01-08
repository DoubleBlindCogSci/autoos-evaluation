from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
rffvf = Factor("rffvf", ["zfi", "rmut"])
xyxhz = Factor("xyxhz", ["qowuql", "tlat"])
tbgx = Factor("tbgx", ["zfi", "rmut"])
yds = Factor("yds", ["qowuql", "tlat"])
constraints = [AtLeastKInARow(4, tbgx), AtMostKInARow(4, xyxhz)]
crossing = [tbgx, xyxhz]

design=[rffvf,xyxhz,tbgx,yds]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_2"))
