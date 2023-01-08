from sweetpea import *
import os
_dir=os.path.dirname(__file__)
rkcso = Factor("rkcso", ["yem", "brbbo"])
zcbpu = Factor("zcbpu", ["mtmxjj", "zgz"])
zrol = Factor("zrol", ["gkxrt", "pbl"])
hgdglc = Factor("hgdglc", ["cmh", "azv"])
constraints = []
crossing = [rkcso, zcbpu, zrol, hgdglc]


design=[rkcso,zcbpu,zrol,hgdglc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_0"))

### END