from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_Hbo = Factor("9Hbo", [Level("mjeM6wMKYIK", 1), Level("UqULnkQ_jBt", 1), Level("ueEbBR$NX1kV}i", 4), Level("X[nF$w;:g", 1), Level("tMGI", 1), Level("SGm", 1), Level("FBovs", 1)])


design=[_Hbo]
crossing=[_Hbo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))

### END
