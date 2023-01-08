from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
P_wsDV__ALK = Factor("P9wsDV|4ALK", [Level("ZZ2DuB", 3), Level("<Avw3cfdY", 7), Level("d umF", 1), Level("WebhKMB", 1), Level("Ih?EvdPw", 1), Level("bkzNVmobGno", 1), Level("(NWTBTwG", 1)])

design=[P_wsDV__ALK]
crossing=[P_wsDV__ALK]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))

### END
