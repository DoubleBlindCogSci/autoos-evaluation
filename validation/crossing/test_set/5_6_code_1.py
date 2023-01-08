from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rrv = Factor("rrv", ["mexo", "rntd"])
irve = Factor("irve", ["tqp", "cko"])
kkiyay = Factor("kkiyay", ["rnac", "naxhv"])
vmwu = Factor("vmwu", ["rdpxi", "sgysbp"])
fqj = Factor("fqj", ["fxcj", "ilf"])

### EXPERIMENT
design=[rrv,irve,kkiyay,vmwu,fqj]
crossing=[[rrv,irve,kkiyay,vmwu,fqj]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_6"))
### END