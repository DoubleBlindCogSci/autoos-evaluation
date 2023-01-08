from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DoWLJQTOfX=["{>KnB","HolRmISDb","CsX QNe4uap"]
JbG3CRe4yIP=Factor('AWfebGIUdJq',DoWLJQTOfX)

### EXPERIMENT
design=[JbG3CRe4yIP]
crossing=[JbG3CRe4yIP]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END