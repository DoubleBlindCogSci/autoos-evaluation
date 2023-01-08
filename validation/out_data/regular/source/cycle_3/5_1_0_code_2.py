from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mUb_ = Factor("mUb5", [Level("hte^5etuv", 1), Level("EROyZw$hUj", 1), Level("mF]", 8), Level("m~hSy", 1), Level("RcM#P", 1)])

design=[mUb_]
crossing=[mUb_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))

### END
