from sweetpea import *
import os
_dir=os.path.dirname(__file__)
tyg = Factor("tyg", ["towc", "vdszg"])
dhc = Factor("dhc", ["uopjew", "oykfj"])
constraints = []
crossing = [tyg, dhc]


design=[tyg,dhc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_4"))

### END