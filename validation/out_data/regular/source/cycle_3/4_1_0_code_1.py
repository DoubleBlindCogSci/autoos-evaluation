from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EROevkptLW_=Factor('L}}zqHgaj',['kXYndZlyBdeD',"ejB Qk","|Gv~N3cNtZp[","JAiapx)cJYsQ"])

### EXPERIMENT
design=[EROevkptLW_]
crossing=[EROevkptLW_]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
### END