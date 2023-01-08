from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eEdlu=[Level("iZEiP",4),';it',Level('ez[RDJxx',4),Level("giO",3)]
h2WU=Factor("xY0YmMZJTM",eEdlu)
ImiLA3j=[Level("kYRAC",5),"byE","nrdAgsrbp","ZgS"]
UiHYnXHUL8=Factor('ijn&HvqnYiIX6*',ImiLA3j)
ADrcBefC=['GBBDPF{','1qrc}SDy','WwjzBxQ:LoX>*',Level('MDgDiSdRJAJcMW',2)]
jsGfZlD3U4=Factor("CgcZmD&XulWR",ADrcBefC)

### EXPERIMENT
design=[h2WU,UiHYnXHUL8,jsGfZlD3U4]
crossing=[h2WU,UiHYnXHUL8,jsGfZlD3U4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_3_1"))
### END