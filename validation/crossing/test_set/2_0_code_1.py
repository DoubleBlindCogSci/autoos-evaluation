from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xtcerk = Factor("xtcerk", ["glvi", "smsb"])
bwgz = Factor("bwgz", ["nckyt", "hyenw"])

### EXPERIMENT
design=[xtcerk,bwgz]
crossing=[[xtcerk,bwgz]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END