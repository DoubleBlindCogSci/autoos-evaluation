from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rkcso = Factor("rkcso", ["yem", "brbbo"])
zcbpu = Factor("zcbpu", ["mtmxjj", "zgz"])
zrol = Factor("zrol", ["gkxrt", "pbl"])
hgdglc = Factor("hgdglc", ["cmh", "azv"])

### EXPERIMENT
design=[rkcso,zcbpu,zrol,hgdglc]
crossing=[[rkcso,zcbpu,zrol,hgdglc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_0"))
### END