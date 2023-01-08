from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
swjKQQwu__B = Factor("swjKQQwu2 B", ["uJY0yz%JgV", "%FZyYaF1", "a]hoV", "alaqU"])
qwJugPAWEC_ = Factor("qwJugPAWEC*", ["ZDOC|u", Level("fGl7", 4), "#D&eRI6OHf", "QQ]faO!CY&"])

design=[swjKQQwu__B,qwJugPAWEC_]
crossing=[swjKQQwu__B,qwJugPAWEC_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))

### END
