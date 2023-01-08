from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rpwkjy = Factor("rpwkjy", ["idspu", "iarpy"])

### EXPERIMENT
design=[rpwkjy]
crossing=[[rpwkjy],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_4"))
### END