from sweetpea import *
import os
_dir=os.path.dirname(__file__)
eaxm = Factor("eaxm", ["oik", "kkrzu"])
cbiu = Factor("cbiu", ["gmtkcw", "vnmfiq"])
constraints = []
crossing = [eaxm, cbiu]


design=[eaxm,cbiu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END