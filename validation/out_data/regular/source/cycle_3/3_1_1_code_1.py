from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KXeJ3t6=Factor('Q(<kRnOFaCCWfc',["OBe_ov",Level('LKXBe',4),"JUbKW:XxXji"])

### EXPERIMENT
design=[KXeJ3t6]
crossing=[KXeJ3t6]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END