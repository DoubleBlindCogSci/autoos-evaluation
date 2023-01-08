from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JSFI = Factor("JSFI", [Level("GM]pIPOG3y", 1), Level("RuyAPVcjS9w", 1), Level("UUJeR}mTelsSt", 1), Level("} AXX", 4), Level("ArmhRNG", 1)])
YOdrl_w = Factor("YOdrl%w", ["OQPCX{~DyQ", "DnHu^H", "Zejt", "9ALXA{", "tjlzFr$ie", "vMHWaCbpJ A"])

design=[JSFI,YOdrl_w]
crossing=[JSFI,YOdrl_w]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))

### END
