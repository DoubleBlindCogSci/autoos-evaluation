from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lddcp = Factor("lddcp", ["kur", "ideiz"])

### EXPERIMENT
design=[lddcp]
crossing=[[lddcp]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_5"))
### END