from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DCL= Factor("DCL", [Level("lw7IVKnD$>", 1), Level("k?>h#", 9), Level("hat", 1), Level("cf|>zm#BmRY%E", 5), Level("ei_uI39rKEyg", 1)])

design=[DCL]
crossing=[DCL]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_1_1"))

### END
