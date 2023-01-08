from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FcUlGzASLNKP_v = Factor("FcUlGzASLNKP(v", [Level("Zo$b<?LHZYsw", 7), Level("BERk[mgcl", 1), Level("mcmW!~OZqd", 8), Level("RHkFRhKFB", 2), Level("tdHW#Ug7mCJTF", 1)])
aG_iGruiEpi = Factor("aG9iGruiEpi", [Level("{ 1N, eNhfUe MH4gx, W:L#SLKyD df", 1), Level("HU0PWfKY|)", 10), Level("qiRL", 1)])
b_arlTT = Factor("b]arlTT", [Level("hR%q", 3), Level("9Os_", 1), Level("5U|SQ", 1), Level("Gxu", 5), Level("fnaZmSKA6", 1)])

design=[FcUlGzASLNKP_v,aG_iGruiEpi,b_arlTT]
crossing=[FcUlGzASLNKP_v,aG_iGruiEpi,b_arlTT]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_0"))

### END
