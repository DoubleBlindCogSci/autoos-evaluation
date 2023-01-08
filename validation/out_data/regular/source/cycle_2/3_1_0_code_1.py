from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
LUMC=Factor("GleKHr",[Level('XmNqYJLXuKtn',7),'gn(i~QTVo[et','vMXdjeP~m;LUjc'])

### EXPERIMENT
design=[LUMC]
crossing=[LUMC]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END