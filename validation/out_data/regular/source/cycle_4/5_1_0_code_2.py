from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xgk = Factor("xgk", [Level("@GpoL$dxjUs0Y", 1), Level("ZAmIaynnlRO", 1), Level("rWMwDV[ciHmrs", 4), Level("9V4", 1), Level("rCr3V97i^t", 1)])

design=[xgk]
crossing=[xgk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))

### END
