from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZTTKcHt_I = Factor("ZTTKcHt<I", [Level("OS|yv{[UpvDa", 9), Level("UMWKNHvJdD", 1), Level("LzSMH", 1), Level("0fo", 1), Level("$JU]GUA", 1), Level("vJYW", 1), Level("CsdovqHpChLd", 1), Level("gSgOSIT", 1)])
bC_X = Factor("bC@X", [Level("tNfwIuKYoqvIFJ", 9), Level("RtrQVwWj(pUY[", 1), Level("aHoK7P", 1), Level("JYtSUk", 1), Level("thgDE]Jp", 1), Level("Mcd xm3e}B", 1), Level("MrrRen$acYzgHf", 1), Level("CuELFAwb", 1)])

design=[ZTTKcHt_I,bC_X]
crossing=[ZTTKcHt_I,bC_X]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_0"))

### END
