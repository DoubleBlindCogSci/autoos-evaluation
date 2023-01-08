from sweetpea import *
import os
_dir=os.path.dirname(__file__)
pzzf = Factor("pzzf", ["vkivv", "eizpo"])
aextjb = Factor("aextjb", ["yea", "ptr"])
bcsp = Factor("bcsp", ["vmj", "aanqn"])
zxehyq = Factor("zxehyq", ["enn", "kxrlzu"])
constraints = []
crossing = [pzzf, aextjb, bcsp, zxehyq]


design=[pzzf,aextjb,bcsp,zxehyq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END