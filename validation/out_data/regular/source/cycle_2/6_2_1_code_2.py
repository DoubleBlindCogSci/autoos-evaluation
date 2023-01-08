from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_kT = Factor("]kT", ["gfno%S!y", "5Ex!Si", "SFuS$^dox]O", "JNM", "FXgs9U;xQ", "cpxjNiurae_P"])
t_toElWzUOfkCN = Factor("t toElWzUOfkCN", [Level("XDQm", 7), Level("8*b2", 1), Level("OVk6EQh", 1), Level("{<T_aIYLJQO", 1), Level("mSb0", 1), Level("&ftzV", 4)])

design=[_kT,t_toElWzUOfkCN]
crossing=[_kT,t_toElWzUOfkCN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))

### END
