from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KHM_we7nHeh=['kKfkVKEAkc',"Qrgm",'NujXNuL',Level('CMl',8),Level("MUMxXxJxFD>)",7),Level('caXvWgB:S',1),"r;bzJL"]
zEj5TtzY=Factor("NS9%aybiO6",KHM_we7nHeh)

### EXPERIMENT
design=[zEj5TtzY]
crossing=[zEj5TtzY]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/7_1_1"))
### END