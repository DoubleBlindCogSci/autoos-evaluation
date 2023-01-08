from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
smpw = Factor("smpw", ["pscw", "uakzm"])
cqi = Factor("cqi", ["ctvo", "dkv"])
jece = Factor("jece", ["isbq", "zpgc"])
zvhyb = Factor("zvhyb", ["mdmqz", "zdpt"])

### EXPERIMENT
design=[smpw,cqi,jece,zvhyb]
crossing=[[smpw,cqi,jece,zvhyb],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END