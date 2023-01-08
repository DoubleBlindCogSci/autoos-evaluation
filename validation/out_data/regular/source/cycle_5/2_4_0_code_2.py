from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Lwp_nnRMKq = Factor("Lwp(nnRMKq", [Level("*vEdLnSHq&?MNu", 1), Level("2kFa", 1)])
GY_ = Factor("GY!", ["L9WVAMPvBvuaZ", "wy5vkP(aiXm"])
RrT_Oh = Factor("RrT(Oh", ["cuqHR)Z6E2@J", "Dtum4"])
yDe_f = Factor("yDe>f", [Level("T^#*bHSDYj", 1), Level("RQ3Qj", 1)])

design=[Lwp_nnRMKq,GY_,RrT_Oh,yDe_f]
crossing=[Lwp_nnRMKq,GY_,RrT_Oh,yDe_f]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4_0"))

### END
