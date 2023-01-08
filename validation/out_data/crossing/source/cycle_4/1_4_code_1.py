from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tyg = Factor("tyg", ["towc", "vdszg"])
dhc = Factor("dhc", ["uopjew", "oykfj"])

### EXPERIMENT
design=[tyg,dhc]
crossing=[[tyg,dhc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_4"))
### END