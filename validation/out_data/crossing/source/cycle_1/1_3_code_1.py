from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hxj = Factor("hxj", ["tfyil", "lzwr"])
ylxg = Factor("ylxg", ["xjmpuv", "eawolz"])

### EXPERIMENT
design=[hxj,ylxg]
crossing=[[hxj,ylxg],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END