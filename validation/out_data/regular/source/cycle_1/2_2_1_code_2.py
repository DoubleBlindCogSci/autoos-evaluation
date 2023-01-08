from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NvWsk_S_Q= Factor("NvWsk&S6Q", ["fGWygGC1", "z9bO"])
usoTdsJdQX= Factor("usoTdsJdQX", [Level("^iAkR", 1), Level(")O8T", 1)])

design=[NvWsk_S_Q,usoTdsJdQX]
crossing=[NvWsk_S_Q,usoTdsJdQX]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/2_2_1"))

### END
