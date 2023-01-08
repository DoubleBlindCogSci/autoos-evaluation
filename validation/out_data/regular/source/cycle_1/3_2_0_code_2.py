from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gVluEr= Factor("gVluEr", [Level("z&F T", 1), Level("Lkn", 5), Level("wAvF(", 1)])
Jo_YFb_gcut__e= Factor("Jo$YFb1gcut;0e", [Level("Wu}Fg:{V", 10), Level("xbzPA", 1), Level("b3EjP", 2)])

design=[gVluEr,Jo_YFb_gcut__e]
crossing=[gVluEr,Jo_YFb_gcut__e]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/3_2_0"))

### END
