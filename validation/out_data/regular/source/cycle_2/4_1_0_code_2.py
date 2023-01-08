from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ieoVqgr = Factor("ieoVqgr", [Level("_*{iCBAnJ2Ki", 2), "dBNmHgf", "HUbCwBk ", "RUJ?z6ZCKik]vL"])

design=[ieoVqgr]
crossing=[ieoVqgr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_0"))

### END
