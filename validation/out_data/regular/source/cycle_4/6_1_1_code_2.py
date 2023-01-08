from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
udetjD = Factor("udetjD",  [Level("fhi1", 3), Level("BY&sLXcP", 1), Level("fbcBJenTtBWNQD", 2), Level("eOQNP^Ko", 1), Level("nWmBG", 1), Level("zyVolwh", 1)])

design=[udetjD]
crossing=[udetjD]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_1"))

### END
