from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ayifa = Factor("ayifa", ["yndyli", "ffhnt"])
xmzy = Factor("xmzy", ["itsxd", "fuhl"])

### EXPERIMENT
design=[ayifa,xmzy]
crossing=[[ayifa,xmzy],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_4"))
### END