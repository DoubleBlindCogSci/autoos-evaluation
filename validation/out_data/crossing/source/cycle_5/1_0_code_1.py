from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
omb = Factor("omb", ["tvd", "yljr"])
zrt = Factor("zrt", ["ojt", "wnsxt"])
tzgze = Factor("tzgze", ["acoyac", "ugd"])

### EXPERIMENT
design=[omb,zrt,tzgze]
crossing=[[omb,zrt,tzgze],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_0"))
### END