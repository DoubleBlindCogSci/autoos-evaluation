from sweetpea import *
import os
_dir=os.path.dirname(__file__)
xtcerk = Factor("xtcerk", ["glvi", "smsb"])
bwgz = Factor("bwgz", ["nckyt", "hyenw"])
constraints = []
crossing = [xtcerk, bwgz]


design=[xtcerk,bwgz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END