from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xY_YmMZJTM= Factor("xY0YmMZJTM", [Level("iZEiP", 4), Level(";it", 1), Level("ez[RDJxx", 4), Level("giO", 3)])
ijn_HvqnYiIX__= Factor("ijn&HvqnYiIX6*", [Level("kYRAC", 5), Level("byE", 1), Level("nrdAgsrbp", 1), Level("ZgS", 1)])
CgcZmD_XulWR= Factor("CgcZmD&XulWR", [Level("GBBDPF{", 1), Level("1qrc}SDy", 1), Level("WwjzBxQ:LoX>*", 1), Level("MDgDiSdRJAJcMW", 2)])

design=[xY_YmMZJTM,ijn_HvqnYiIX__,CgcZmD_XulWR]
crossing=[xY_YmMZJTM,ijn_HvqnYiIX__,CgcZmD_XulWR]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_3_1"))

### END
