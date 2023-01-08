from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xvY = Factor("xvY", [Level("kTgCBo", 3), "dZoO$8Z]uxw[eF", "utXNld?AdXwG", "kg4JqTq%Yt", "PjfbyGLBPRltWg"])
IVH = Factor("IVH", ["fG^swtQYm", "mgUjZ?", ";gJBl:P", Level("UWneV", 2)])
bC_DNg = Factor("bC3DNg", ["lpPrq", "BYDwlOTzPr", "]czuP", Level("z4wIcQE", 1)])
UKGjSSoVt = Factor("UKGjSSoVt", ["Buzg", "aj^p:e", "cZFN", Level("jCG;fMVo", 1)])

design=[xvY,IVH,bC_DNg,UKGjSSoVt]
crossing=[xvY,IVH,bC_DNg,UKGjSSoVt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_4_1"))

### END
