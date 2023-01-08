from sweetpea import *
import os
_dir=os.path.dirname(__file__)
zzfdzo = Factor("zzfdzo", ["bvw", "ceswj"])
constraints = []
crossing = [zzfdzo]


design=[zzfdzo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END