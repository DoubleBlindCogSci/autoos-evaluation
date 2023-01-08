from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rqetz = Factor("rqetz", ["yqdam", "emmx"])
ltds = Factor("ltds", ["vckft", "oktczp"])

### EXPERIMENT
constraints=[AtMostKInARow(2,(rqetz,"emmx"))]
design=[rqetz,ltds]
crossing=[ltds]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_4"))
### END