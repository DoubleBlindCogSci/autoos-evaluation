from sweetpea import *
import os
_dir=os.path.dirname(__file__)
gvbikm = Factor("gvbikm", ["lvxawc", "hxo"])
wfq = Factor("wfq", ["frnxop", "hcu"])
cqz = Factor("cqz", ["rbpmrs", "aclm"])
constraints = []
crossing = [gvbikm, wfq, cqz]


design=[gvbikm,wfq,cqz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_4"))

### END