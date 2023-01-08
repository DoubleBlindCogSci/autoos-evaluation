from sweetpea import *
import os
_dir=os.path.dirname(__file__)
smpw = Factor("smpw", ["pscw", "uakzm"])
cqi = Factor("cqi", ["ctvo", "dkv"])
jece = Factor("jece", ["isbq", "zpgc"])
zvhyb = Factor("zvhyb", ["mdmqz", "zdpt"])
constraints = []
crossing = [smpw, cqi, jece, zvhyb]


design=[smpw,cqi,jece,zvhyb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END