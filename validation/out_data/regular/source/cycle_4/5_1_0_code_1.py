from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
SF6ybDO=Factor('xgk',['@GpoL$dxjUs0Y',"ZAmIaynnlRO",Level('rWMwDV[ciHmrs',4),'9V4','rCr3V97i^t'])

### EXPERIMENT
design=[SF6ybDO]
crossing=[SF6ybDO]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
### END