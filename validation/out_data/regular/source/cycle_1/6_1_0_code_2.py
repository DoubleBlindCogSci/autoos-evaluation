from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OTgMpKkL_zlO= Factor("OTgMpKkL6zlO", [Level("mBE", 1), Level("qhvNtvZNEqAUq", 2), Level("Onn", 6), Level("PMX*Sfq", 8), Level("hTTo", 10), Level("SWu[TkRKLePSRF", 1)])

design=[OTgMpKkL_zlO]
crossing=[OTgMpKkL_zlO]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_1_0"))

### END
