from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
QsiCS_NyiKOI = Factor("QsiCS>NyiKOI", [Level("u7SXgrVA", 1), Level("Hd6AZsP FXzpp", 1), Level("QvwsJ!LQQh^", 1), Level("g$Tw$|hD", 1), Level("gkOA", 4), Level("FyJIroW ", 1), Level("5fB", 7)])
yVhWORI_ybTCAg = Factor("yVhWORI$ybTCAg", ["qEFFZyBFt", "[C8@TLkuV", "NuvEuCcGONdo)", "ZWkLap&c|*", "fG4JV", "LKsyttOx#nmMW"])
wnyiy = Factor("wnyiy", [Level("oOVc]WxP", 1), Level("fAM", 10), Level("mi}vqR8C[A", 1), Level("D?vL*lPpIlXcoZ", 6), Level("MtYptrglyal", 4), Level("gUxcnoK", 1), Level("#ozHPj%", 2)])

design=[QsiCS_NyiKOI,yVhWORI_ybTCAg,wnyiy]
crossing=[QsiCS_NyiKOI,yVhWORI_ybTCAg,wnyiy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_1"))

### END
