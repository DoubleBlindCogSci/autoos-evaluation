from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
v_J= Factor("v_J", [Level("bZmcE@I", 1), Level("dLlbWhO;", 1), Level("HHZnXj", 1), Level("JI%%REE", 1), Level("ZoJ", 1), Level("WOCPPJJl*YLWJ$", 1), Level("rDsKX~hRgl", 1), Level("DWOBAyAQ", 1), Level("X8wvcPgdMeVX", 10)])

design=[v_J]
crossing=[v_J]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/9_1_1"))

### END
