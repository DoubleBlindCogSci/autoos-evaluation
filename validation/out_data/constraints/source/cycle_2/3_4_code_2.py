from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
apzs = Factor("apzs", ["sjnzhf","pydes","avo", "gooen"])
rzcr = Factor("rzcr", ["ffgfn","fqw", "kpgbi"])
cfycbu = Factor("cfycbu", ["fqnxz","ynqh", "jcfdy"])
eptgp = Factor("eptgp", ["ftbfhn","vxkf", "qtxj"])


constraints = [Exclude((apzs, "gooen")), AtLeastKInARow(4, (rzcr, "kpgbi")), AtMostKInARow(2, (cfycbu, "jcfdy"))]
crossing = [eptgp]

design=[apzs,rzcr,cfycbu,eptgp]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4"))

### END