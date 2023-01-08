from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
a_OhH_ = Factor("a;OhH3", ["#kgly", "FMZZS", "KBZFZihZt&QlNv", "OxQQ%WI"])

design=[a_OhH_]
crossing=[a_OhH_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))

### END
