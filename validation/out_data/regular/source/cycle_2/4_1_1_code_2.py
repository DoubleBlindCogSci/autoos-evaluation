from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
emTcasNQXB = Factor("emTcasNQXB", [Level("bRfDrY", 1), Level("}NtZuYPVKQsZz", 1), Level("HQHGo@8idP", 2), Level("kTQcBUmp", 3), Level("UhU", 1)])

design=[emTcasNQXB]
crossing=[emTcasNQXB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))

### END
