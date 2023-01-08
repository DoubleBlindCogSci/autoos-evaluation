from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vkc = Factor("vkc", ["mvjae", "pnsel"])
ztibii = Factor("ztibii", ["zmfxn", "gvwgzi"])

### EXPERIMENT
design=[vkc,ztibii]
crossing=[[vkc],[ztibii],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_5"))
### END