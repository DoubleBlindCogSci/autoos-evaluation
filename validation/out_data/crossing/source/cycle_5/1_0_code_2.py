from sweetpea import *
import os
_dir=os.path.dirname(__file__)
omb = Factor("omb", ["tvd", "yljr"])
zrt = Factor("zrt", ["ojt", "wnsxt"])
tzgze = Factor("tzgze", ["acoyac", "ugd"])
constraints = []
crossing = [omb, zrt, tzgze]


design=[omb,zrt,tzgze]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_0"))

### END