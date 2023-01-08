from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rczadd = Factor("rczadd", ["dvwn", "zwt"])
xjaz = Factor("xjaz", ["eiz", "vzvgva"])

### EXPERIMENT
design=[rczadd,xjaz]
crossing=[[rczadd,xjaz]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1"))
### END