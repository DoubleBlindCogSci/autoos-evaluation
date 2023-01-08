from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
oyi = Factor("oyi", ["cjtg", "hpmo"])
gxqk = Factor("gxqk", ["rfk", "usnhq"])
holhg = Factor("holhg", ["cjtg", "hpmo"])
wpl = Factor("wpl", ["rfk", "usnhq"])
ngp = Factor("ngp", ["qqk", "eqpc"])
design=[oyi,gxqk,holhg,wpl,ngp]
constraints=[MinimumTrials(16),AtMostKInARow(4, ngp)]
crossing=[gxqk,holhg]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_2"))
