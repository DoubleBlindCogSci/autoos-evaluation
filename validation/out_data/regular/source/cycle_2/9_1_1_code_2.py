from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZbaD = Factor("ZbaD", [Level("jhCRI)YIX", 1), Level("GLuI", 1), Level("mLFWURTN4pNq", 5), Level("KgcuDbbXobSPwu", 1), Level("vYNuY}CJPxNTli", 6), Level("dFJ[tHB", 1), Level("HukXRhVF", 1), Level("xthWfHGq", 1), Level("EkUmun(kp", 1)])

design=[ZbaD]
crossing=[ZbaD]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_1_1"))

### END
