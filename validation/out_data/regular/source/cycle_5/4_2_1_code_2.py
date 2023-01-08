from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jrBPlmfLSpWsF = Factor("jrBPlmfLSpWsF", [Level("se?IrKzJrDI", 3), Level("i1X", 1), Level("K5OVr>{:~b|>k", 1), Level("eFC", 1)])
FXN = Factor("FXN", [Level("K>bb7Z7B", 1), Level("JzEhZ", 1), Level("ZyGndX~hiq", 1), Level("!eTCyRRlSjR4d", 3)])

design=[jrBPlmfLSpWsF,FXN]
crossing=[jrBPlmfLSpWsF,FXN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))

### END
