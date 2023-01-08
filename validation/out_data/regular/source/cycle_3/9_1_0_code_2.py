from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IBDVkH = Factor("IBDVkH", [Level("vvp", 1), Level("MO<Y:2w9&L", 1), Level("2uZqVCxLgF", 1), Level("piWiEwOAGus", 1), Level("yOXTOW", 3), Level("xqO", 1), Level("eOGELHT0npm", 2), Level("u2n:lR", 9), Level("YcDBOFK", 7)])

design=[IBDVkH]
crossing=[IBDVkH]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_1_0"))

### END
