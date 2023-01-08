from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
psy = Factor("psy", ["fbiam", "ivo"])
vbgn = Factor("vbgn", ["stlz", "vlrhyy"])
qxnli = Factor("qxnli", ["uedbcr", "ybu"])

### EXPERIMENT
design=[psy,vbgn,qxnli]
crossing = [[psy,vbgn],[qxnli],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1"))
### END
