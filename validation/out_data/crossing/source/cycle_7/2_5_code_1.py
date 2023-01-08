from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ghpv = Factor("ghpv", ["eyw", "iyhkv"])
ddgbqq = Factor("ddgbqq", ["cngwv", "udtga"])

### EXPERIMENT
design=[ghpv,ddgbqq]
crossing=[[ghpv,ddgbqq]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_5"))
### END