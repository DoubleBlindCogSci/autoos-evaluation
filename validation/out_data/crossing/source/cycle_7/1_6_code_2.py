from sweetpea import *
import os
_dir=os.path.dirname(__file__)
stci = Factor("stci", ["atgbx", "xnfbi"])
constraints = []
crossing = [stci]


design=[stci]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_6"))

### END