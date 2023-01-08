from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

Vv_lOMVY_ = Factor("Vv)lOMVY(", ["AmJ(F@ohUpCS]", "p4D", "Lw}YpK%", "rkHSip"])


design=[Vv_lOMVY_]
crossing=[Vv_lOMVY_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_0"))

### END
