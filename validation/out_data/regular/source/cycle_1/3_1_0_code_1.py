from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NXq6C2MVkpu=Factor("4RIQWYuowl~h",[Level('K%XmcFtaabZq',4),Level('4Ahlxy',9),"DT359X[Qb<wW"])

### EXPERIMENT
design=[NXq6C2MVkpu]
crossing=[NXq6C2MVkpu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/3_1_0"))
### END