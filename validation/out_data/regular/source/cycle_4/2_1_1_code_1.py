from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xLOnKhS=Factor('TIZQaerItG?',["iot",'wpUnX'])

### EXPERIMENT
design=[xLOnKhS]
crossing=[xLOnKhS]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END