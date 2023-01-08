from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fhy = Factor("fhy", ["tao", "anh"])

### EXPERIMENT
design=[fhy]
crossing=[[fhy]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_7"))
### END