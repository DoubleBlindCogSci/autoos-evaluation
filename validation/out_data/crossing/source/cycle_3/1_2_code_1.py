from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cgt = Factor("cgt", ["roztnp", "psgyum"])
vuumjc = Factor("vuumjc", ["kgb", "zkjo"])
thgj = Factor("thgj", ["lrlv", "jpxk"])
ekbj = Factor("ekbj", ["ony", "mgud"])

### EXPERIMENT
design=[cgt,vuumjc,thgj,ekbj]
crossing=[[cgt,vuumjc,thgj,ekbj],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_2"))
### END