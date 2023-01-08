from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
W_X = Factor("W]X", [Level("u&j", 8), Level("Irw ]", 1), Level("cP)", 1)])
_v_uhf = Factor("*v(uhf", ["h}[xOnoj", "nGc", "KxpqG"])

design=[W_X,_v_uhf]
crossing=[W_X,_v_uhf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
