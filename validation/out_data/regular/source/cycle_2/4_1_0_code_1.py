from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Qi3DHh=Factor('ieoVqgr',["dBNmHgf",Level("_*{iCBAnJ2Ki",2),'HUbCwBk ',"RUJ?z6ZCKik]vL"])

### EXPERIMENT
design=[Qi3DHh]
crossing=[Qi3DHh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
### END