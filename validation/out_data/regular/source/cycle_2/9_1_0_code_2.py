from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vqm = Factor("vqm", [Level("jPf>W VZUAH", 1), Level("LGtSt)N", 1), Level("BLU", 1), Level("8ytB", 1), Level("LyR8vweV", 1), Level("|IhadODzeOW", 1), Level("Z@^YYRLr", 7), Level("ecIX>", 1), Level("r*wMCeJZjUX", 1)])

design=[vqm]
crossing=[vqm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_1_0"))

### END
