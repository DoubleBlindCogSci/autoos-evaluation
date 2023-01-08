from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_XkYk = Factor("$XkYk", [Level("XuaQS$gQZ", 6), Level("Pz!prPZ*j po", 1), Level("uQ~WM}%poZCY", 1), Level("2dAGZcyq]MX", 1), Level("twP", 4), Level("KUXy XBS", 1), Level("aofcpBsALYE", 3), Level("wiMOx7:", 1)])
BpAj = Factor("BpAj", [Level("BeOqqMlr}x", 6), Level("~VoK", 4), Level("YCW", 1), Level("qynojic", 4), Level("%YH", 1), Level("XAFx", 1), Level("YiY{M;n_cZ", 1), Level("BvMx hh$w_[", 6), Level("dwczRb9", 1)])

design=[_XkYk,BpAj]
crossing=[_XkYk,BpAj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_1"))

### END
