from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CxEjz= Factor("CxEjz", [Level("jCYEbtvELwwE*o", 8), Level("myFH", 1), Level("ymHJiHBNgE", 1), Level("J2FUQ", 1)])

design=[CxEjz]
crossing=[CxEjz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_1_1"))

### END
