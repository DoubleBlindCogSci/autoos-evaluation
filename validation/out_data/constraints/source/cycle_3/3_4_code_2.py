from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ogbl = Factor("ogbl", ["etudac","wxt", "jkb"])
teyclb = Factor("teyclb", ["bxfpd", "kuu"])
bxxl = Factor("bxxl", ["awfv", "hmbn"])
xzh = Factor("xzh", ["cxys","aqh","dlfx", "wlohoa"])
mant = Factor("mant", ["hwx", "iodnw"])
ugyl = Factor("ugyl", ["fpneis","hbnb", "swvspa"])


constraints = [ExactlyK(2, (ogbl, "jkb")), Exclude((teyclb, "kuu")), ExactlyK(3, (bxxl, "hmbn"))]
crossing = [xzh, mant, ugyl]

design=[ogbl,teyclb,bxxl,xzh,mant,ugyl]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4"))

### END