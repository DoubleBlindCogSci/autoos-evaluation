from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Mi2ahq=Factor('a;OhH3',["#kgly","FMZZS","KBZFZihZt&QlNv",'OxQQ%WI'])

### EXPERIMENT
design=[Mi2ahq]
crossing=[Mi2ahq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
### END