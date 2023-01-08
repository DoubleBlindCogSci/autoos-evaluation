from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_RIQWYuowl_h= Factor("4RIQWYuowl~h", [Level("K%XmcFtaabZq", 4), Level("4Ahlxy", 9), Level("DT359X[Qb<wW", 1)])


design=[_RIQWYuowl_h]
crossing=[_RIQWYuowl_h]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/3_1_0"))

### END
