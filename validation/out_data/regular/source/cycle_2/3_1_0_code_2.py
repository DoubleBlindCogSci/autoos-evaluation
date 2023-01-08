from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GleKHr = Factor("GleKHr", [Level("XmNqYJLXuKtn", 7), Level("gn(i~QTVo[et", 1), Level("vMXdjeP~m;LUjc", 1)])

design=[GleKHr]
crossing=[GleKHr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
