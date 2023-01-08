from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OpS = Factor("OpS", ["2tXWexZ", "dSH|hlFVObONk"])
e_WxsEDEWgDMz = Factor("e0WxsEDEWgDMz", [Level("wgFdahXpLHV", 10), Level("q;dRnYDA", 1)])

design=[OpS,e_WxsEDEWgDMz]
crossing=[OpS,e_WxsEDEWgDMz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
