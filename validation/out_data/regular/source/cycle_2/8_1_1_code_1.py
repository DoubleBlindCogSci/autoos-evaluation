from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cfrhkI=Factor("E2QybeIzTbmE",[Level("Ps4solx7LQp",7),'gU2zjVj',"Mj*w%D_UzPCNCN","PSwRQC","jG4","PnChNip^E b",Level('ZQwwn',1),Level("fDr",7)])

### EXPERIMENT
design=[cfrhkI]
crossing=[cfrhkI]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_1"))
### END