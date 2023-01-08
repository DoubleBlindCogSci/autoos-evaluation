from sweetpea import *
import os
_dir=os.path.dirname(__file__)
quhze = Factor("quhze", ["obyy", "ldvlq"])
lpa = Factor("lpa", ["xqosg", "gmktwf"])
constraints = []
crossing = [quhze, lpa]


design=[quhze,lpa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_1"))

### END