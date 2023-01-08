from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tXW= Factor("tXW", ["~GhW0Y$Nkgrt", "yjS"])

design=[tXW]
crossing=[tXW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/2_1_0"))

### END
