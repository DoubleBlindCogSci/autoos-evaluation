from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
finB=Level("zvuocncr",1)
bd4HuCXn2o='DzwmD>o'
VhoqxpdmAzY=Factor('[Tq',[finB,'qcGjlkq','im8(l',Level("quiBMqJ)",1),"tucqET6x}9",bd4HuCXn2o,"IWLU",'!IB'])

### EXPERIMENT
design=[VhoqxpdmAzY]
crossing=[VhoqxpdmAzY]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
### END