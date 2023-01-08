from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
E_QybeIzTbmE = Factor("E2QybeIzTbmE", [Level("Ps4solx7LQp", 7), Level("gU2zjVj", 1), Level("Mj*w%D_UzPCNCN", 1), Level("PSwRQC", 1), Level("jG4", 1), Level("PnChNip^E b", 1), Level("ZQwwn", 1), Level("fDr", 7)])

design=[E_QybeIzTbmE]
crossing=[E_QybeIzTbmE]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_1"))

### END
