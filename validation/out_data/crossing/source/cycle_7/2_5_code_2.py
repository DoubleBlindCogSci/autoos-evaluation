from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ghpv = Factor("ghpv", ["eyw", "iyhkv"])
ddgbqq = Factor("ddgbqq", ["cngwv", "udtga"])
constraints = []
crossing = [ghpv, ddgbqq]


design=[ghpv,ddgbqq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_5"))

### END