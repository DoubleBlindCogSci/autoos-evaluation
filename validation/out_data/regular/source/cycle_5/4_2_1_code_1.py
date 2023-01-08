from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
o5TUnA=Factor('jrBPlmfLSpWsF',[Level("se?IrKzJrDI",3),"i1X","K5OVr>{:~b|>k","eFC"])
bQbC9w0riF=Factor('FXN',["K>bb7Z7B","JzEhZ",'ZyGndX~hiq',Level('!eTCyRRlSjR4d',3)])

### EXPERIMENT
design=[o5TUnA,bQbC9w0riF]
crossing=[o5TUnA,bQbC9w0riF]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_1"))
### END