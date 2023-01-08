from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_nMFHmg = Factor("6nMFHmg", [Level("U RPg", 1), Level("U>eAy", 9), Level("nMBLBD", 6), "TFPr7Azswr", "deEUu", "hqp", "%ZoTnVTIe&", "M:z]GH"])
RryaCHD_QG = Factor("RryaCHD<QG", [Level("lqAK4QobG_zBVR", 2), Level("isRd", 1), Level("PNm", 2), "BMMmNTpyMD", "}dzpC8", "i$Nm", Level("BMPhQNUw", 8), "DGIUu}"])


design=[_nMFHmg,RryaCHD_QG]
crossing=[_nMFHmg,RryaCHD_QG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_0"))

### END
