from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CMbnP=["~GhW0Y$Nkgrt",'yjS']
IVcrmwQgZQ=Factor('tXW',CMbnP)

### EXPERIMENT
design=[IVcrmwQgZQ]
crossing=[IVcrmwQgZQ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/2_1_0"))
### END