from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
z_= Factor("z)", [Level("Exg[AC?ZBF&G", 1), Level("LffPu", 3), Level("k{Bsw:", 1), Level("z3o@a", 1), Level(")gl", 4), Level("mGH]feSN@E_wZ", 1), Level("} SXCLk", 1), Level("EpPGNSOMX|ID&", 1), Level("w3JkLFy!ykO]", 8)])

design=[z_]
crossing=[z_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/8_1_0"))

### END
