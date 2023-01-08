from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BiXDXCLlL=Factor(")xywqJoUzh",["NuE2","WAt",Level('W66ltFgIjag',4)])
BSsCidLJ6=Factor("?brQB",['SzcCqu(]SLL8',Level('NVW(',4),'(@kYc'])

### EXPERIMENT
design=[BiXDXCLlL,BSsCidLJ6]
crossing=[BiXDXCLlL,BSsCidLJ6]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END