from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
foXuvv1T5cO=Factor('CxEjz',[Level('jCYEbtvELwwE*o',8),'myFH','ymHJiHBNgE',"J2FUQ"])

### EXPERIMENT
design=[foXuvv1T5cO]
crossing=[foXuvv1T5cO]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_1_1"))
### END