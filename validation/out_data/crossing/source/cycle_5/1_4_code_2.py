from sweetpea import *
import os
_dir=os.path.dirname(__file__)
rpwkjy = Factor("rpwkjy", ["idspu", "iarpy"])
constraints = []
crossing = [rpwkjy]


design=[rpwkjy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_4"))

### END