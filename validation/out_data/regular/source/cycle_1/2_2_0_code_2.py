from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
XhhZiGB= Factor("XhhZiGB", [Level("hPGl uOtisLND", 6), Level("syCRDMI", 1)])
uXUzDyTLRmY= Factor("uXUzDyTLRmY", ["&WZJORykj__bx<", "yvbPMPvTBO"])

design=[XhhZiGB,uXUzDyTLRmY]
crossing=[XhhZiGB,uXUzDyTLRmY]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/2_2_0"))

### END
