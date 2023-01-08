from sweetpea import *
import os
_dir=os.path.dirname(__file__)
rczadd = Factor("rczadd", ["dvwn", "zwt"])
xjaz = Factor("xjaz", ["eiz", "vzvgva"])
constraints = []
crossing = [rczadd, xjaz]


design=[rczadd,xjaz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END