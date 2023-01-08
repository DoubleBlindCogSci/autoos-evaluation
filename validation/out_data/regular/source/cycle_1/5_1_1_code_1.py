from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KHhgwB=['lw7IVKnD$>',Level("k?>h#",9),'hat',Level("cf|>zm#BmRY%E",5),'ei_uI39rKEyg']
AGkm432hcD=Factor('DCL',KHhgwB)

### EXPERIMENT
design=[AGkm432hcD]
crossing=[AGkm432hcD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_1_1"))
### END