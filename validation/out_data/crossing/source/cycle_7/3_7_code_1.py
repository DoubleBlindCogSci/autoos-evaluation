from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uzrqw = Factor("uzrqw", ["lfonws", "mvrwab"])
laa = Factor("laa", ["akvy", "sqzwby"])
immsr = Factor("immsr", ["cposf", "nger"])

### EXPERIMENT
design=[uzrqw,laa,immsr]
crossing=[[uzrqw,laa,immsr]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_7"))
### END