from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
owjqdg = Factor("owjqdg", ["owg", "donn"])
bozkhq = Factor("bozkhq", ["khzpxz", "qovi"])
ziijhw = Factor("ziijhw", ["hmaa", "hynrt"])

### EXPERIMENT
design=[owjqdg,bozkhq,ziijhw]
crossing=[[owjqdg,bozkhq,ziijhw]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_5"))
### END