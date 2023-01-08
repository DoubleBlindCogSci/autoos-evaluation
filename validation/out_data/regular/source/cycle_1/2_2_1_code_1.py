from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Jbz6lL=Factor('NvWsk&S6Q',['fGWygGC1','z9bO'])
Uvy9KTRw1JW=Factor("usoTdsJdQX",[Level("^iAkR",1),')O8T'])

### EXPERIMENT
design=[Jbz6lL,Uvy9KTRw1JW]
crossing=[Jbz6lL,Uvy9KTRw1JW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/2_2_1"))
### END