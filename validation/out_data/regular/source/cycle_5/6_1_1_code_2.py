from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

TJOpNGo_ = Factor("TJOpNGo)",  ["SbqF*Urr*f", "UR@", "~AAJpmVvWE", "nvTlf_a", " <V", "vYwMJ"])


design=[TJOpNGo_]
crossing=[TJOpNGo_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))

### END
