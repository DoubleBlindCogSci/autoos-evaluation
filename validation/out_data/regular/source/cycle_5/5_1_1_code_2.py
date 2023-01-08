from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HzG_aYol = Factor("HzG3aYol",  ["}OLLHVQuFB", "Wdas", "iqGaiGASGpm", "Onc", "eNM", "ccXS2SxY4MQ"])

design=[HzG_aYol]
crossing=[HzG_aYol]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_1"))

### END
