from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VRZp4G8aFHH=Factor('OTgMpKkL6zlO',['mBE',Level("qhvNtvZNEqAUq",2),Level("Onn",6),Level("PMX*Sfq",8),'hTTo',Level("SWu[TkRKLePSRF",10)])

### EXPERIMENT
design=[VRZp4G8aFHH]
crossing=[VRZp4G8aFHH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_1_0"))
### END