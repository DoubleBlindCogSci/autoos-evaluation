from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
__BI_g_XF = Factor("{%BI_g6XF", ["jyii", "HZ3Qv "])
cEO_VAKx = Factor("cEO)VAKx", [Level("p&PLjSRFjie%#1", 1), Level("_{EOfzrFhKw@9R", 4)])

design=[__BI_g_XF,cEO_VAKx]
crossing=[__BI_g_XF,cEO_VAKx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
