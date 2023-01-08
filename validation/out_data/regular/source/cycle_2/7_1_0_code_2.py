from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uTKWUt_ = Factor("uTKWUt~", [Level("aoiY", 9), Level("emXsgJ", 5), Level("rTzHUKCjy;UV", 1), Level("tEQa", 1), Level("QRupXSx", 1), Level("x0ws", 1), Level("qYPbaQ_", 1)])

design=[uTKWUt_]
crossing=[uTKWUt_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_0"))

### END
