from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JarEPo = Factor("JarEPo", [Level("VzUCehpBnaP", 3), Level("uDBGgsjDf2Q", 1), Level("vTxdbNj", 9), Level("ua9E} f", 1), Level("1tGp2tK", 5)])

design=[JarEPo]
crossing=[JarEPo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))

### END
