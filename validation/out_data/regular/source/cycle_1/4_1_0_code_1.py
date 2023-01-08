from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bcYbOuQB4=Factor("iVRovMGdzNfOdK",["I{v&4DOXZf","#hM",'J7G',"v6Mn~RkqfVXp"])

### EXPERIMENT
design=[bcYbOuQB4]
crossing=[bcYbOuQB4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_1_0"))
### END