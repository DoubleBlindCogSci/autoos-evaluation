from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Q__kRnOFaCCWfc = Factor("Q(<kRnOFaCCWfc", [Level("OBe_ov", 1), Level("LKXBe", 4), Level("JUbKW:XxXji", 1)])

design=[Q__kRnOFaCCWfc]
crossing=[Q__kRnOFaCCWfc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
