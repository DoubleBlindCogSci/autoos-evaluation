from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
UVq_fEbnWkk = Factor("UVq[fEbnWkk", [Level("KiLzF", 5), Level("tiYQydlil>", 1), Level("I13", 1), Level("QMoi@D", 7)])
P_WfL_UX_iOyf = Factor("P3WfL]UX>iOyf", ["DpD*VprHYcl", "#Si!7ZG", "dagYxP", "AmTaWIpRQ"])
cuuvWqk_xRA = Factor("cuuvWqk (x)RA", [Level("ZTaZOVVLK", 1), Level("IZ8", 2), Level("3bB%KC3xHUf", 3), Level("WSG;T>D5af{D4B", 1)])

design=[UVq_fEbnWkk,P_WfL_UX_iOyf,cuuvWqk_xRA]
crossing=[UVq_fEbnWkk,P_WfL_UX_iOyf,cuuvWqk_xRA]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_1"))

### END
