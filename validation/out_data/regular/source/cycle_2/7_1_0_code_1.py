from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mHf81x5p=Factor('uTKWUt~',["rTzHUKCjy;UV",Level("aoiY",9),"tEQa",'QRupXSx',Level("x0ws",1),Level("emXsgJ",5),"qYPbaQ_"])

### EXPERIMENT
design=[mHf81x5p]
crossing=[mHf81x5p]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_0"))
### END