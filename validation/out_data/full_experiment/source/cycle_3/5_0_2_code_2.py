from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
oyi = Factor("oyi", ["cjtg", "hpmo"])
gxqk = Factor("gxqk", ["rfk", "usnhq"])
holhg = Factor("holhg", ["cjtg", "hpmo"])
wpl = Factor("wpl", ["rfk", "usnhq"])
ngp = Factor("ngp", ["qqk", "eqpc"])
constraints = [AtMostKInARow(4, ngp), MinimumTrials(16)]
crossing = [gxqk, holhg]

design=[oyi,gxqk,holhg,wpl,ngp]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_0_2"))
