from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Uybr = Factor("Uybr", [Level("ATLpPSw", 1), Level("wdggRlqel", 6), Level("Qyrg", 1), Level("hWjSp", 1), Level("O_ROUCgFYDZ", 10), Level("dowiczkYJJkj(l", 1), Level("t#R", 9)])
rTwGA = Factor("rTwGA", [Level("]&TGB5mxRSCB", 4), Level("Dyavv|3C", 1), Level("bRuwGpkMq", 1), Level("eIkREvKl|Dvr", 6), Level("u><HLRg7ISu", 1), Level("Kfx}VMlifM", 1)])

design=[Uybr,rTwGA]
crossing=[Uybr,rTwGA]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))

### END
