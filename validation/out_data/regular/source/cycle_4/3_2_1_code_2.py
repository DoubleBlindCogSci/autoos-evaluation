from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_xywqJoUzh = Factor(")xywqJoUzh", [Level("NuE2", 1), Level("WAt", 1), Level("W66ltFgIjag", 4)])
_brQB = Factor("?brQB", [Level("SzcCqu(]SLL8", 1), Level("NVW(", 4), Level("(@kYc", 1)])

design=[_xywqJoUzh,_brQB]
crossing=[_xywqJoUzh,_brQB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
