from sweetpea import *
import os
_dir=os.path.dirname(__file__)
uzrqw = Factor("uzrqw", ["lfonws", "mvrwab"])
laa = Factor("laa", ["akvy", "sqzwby"])
immsr = Factor("immsr", ["cposf", "nger"])
constraints = []
crossing = [uzrqw, laa, immsr]


design=[uzrqw,laa,immsr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_7"))

### END