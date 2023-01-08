from sweetpea import *
import os
_dir=os.path.dirname(__file__)
vkc = Factor("vkc", ["mvjae", "pnsel"])
ztibii = Factor("ztibii", ["zmfxn", "gvwgzi"])
constraints = []
crossing = [vkc, ztibii]


design=[vkc,ztibii]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_5"))

### END