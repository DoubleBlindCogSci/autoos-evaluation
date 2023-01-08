from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NS__aybiO_= Factor("NS9%aybiO6", [Level("kKfkVKEAkc", 1), Level("Qrgm", 1), Level("NujXNuL", 1), Level("CMl", 8), Level("MUMxXxJxFD>)", 7), Level("caXvWgB:S", 1), Level("r;bzJL", 1)])

design=[NS__aybiO_]
crossing=[NS__aybiO_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/7_1_1"))

### END
