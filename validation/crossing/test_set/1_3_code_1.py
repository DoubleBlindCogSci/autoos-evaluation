from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
naz = Factor("naz", ["tlis", "dma"])

### EXPERIMENT
design=[naz]
crossing=[[naz]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END