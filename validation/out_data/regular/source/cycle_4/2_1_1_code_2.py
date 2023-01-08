from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TIZQaerItG_ = Factor("TIZQaerItG?", ["iot", "wpUnX"])

design=[TIZQaerItG_]
crossing=[TIZQaerItG_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
