from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eaxm = Factor("eaxm", ["oik", "kkrzu"])
cbiu = Factor("cbiu", ["gmtkcw", "vnmfiq"])

### EXPERIMENT
design=[eaxm,cbiu]
crossing=[[eaxm,cbiu]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2"))
### END