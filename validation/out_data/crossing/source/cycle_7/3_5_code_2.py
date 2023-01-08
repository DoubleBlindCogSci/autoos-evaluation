from sweetpea import *
import os
_dir=os.path.dirname(__file__)
owjqdg = Factor("owjqdg", ["owg", "donn"])
bozkhq = Factor("bozkhq", ["khzpxz", "qovi"])
ziijhw = Factor("ziijhw", ["hmaa", "hynrt"])
constraints = []
crossing = [owjqdg, bozkhq, ziijhw]


design=[owjqdg,bozkhq,ziijhw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_5"))

### END