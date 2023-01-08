from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xlIWPLUam=Factor('v0rAT@nh4lUa',["34PT:","JBSwK"])
O8Vuzp=Factor('W@X',['yS:_','!SkhjvoEViHn'])

### EXPERIMENT
design=[xlIWPLUam,O8Vuzp]
crossing=[xlIWPLUam,O8Vuzp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END