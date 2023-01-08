from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_Tq = Factor("[Tq", [Level("zvuocncr", 1), Level("qcGjlkq", 1), Level("im8(l", 1), Level("quiBMqJ)", 1), Level("tucqET6x}9", 1), Level("DzwmD>o", 1), Level("IWLU", 1), Level("!IB", 1)])

design=[_Tq]
crossing=[_Tq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))

### END
