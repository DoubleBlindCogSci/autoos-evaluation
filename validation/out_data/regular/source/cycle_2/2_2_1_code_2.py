from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
v_rAT_nh_lUa = Factor("v0rAT@nh4lUa", ["34PT:", "JBSwK"])
W_X = Factor("W@X", ["yS:_", "!SkhjvoEViHn"])

design=[v_rAT_nh_lUa,W_X]
crossing=[v_rAT_nh_lUa,W_X]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
