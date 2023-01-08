from sweetpea import *
import os
_dir=os.path.dirname(__file__)
psy = Factor("psy", ["fbiam", "ivo"])
vbgn = Factor("vbgn", ["stlz", "vlrhyy"])
qxnli = Factor("qxnli", ["uedbcr", "ybu"])
constraints = []
crossing = [[psy, vbgn],[ qxnli],]


design=[psy,vbgn,qxnli]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END
