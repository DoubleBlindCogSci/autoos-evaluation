from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_tlmBMqKyTQpk = Factor("@tlmBMqKyTQpk", [Level("y1IloF:khMSw5T", 2), "LSk", "aU{y>>Kz", "5AK", "ggttkmK5gLyw", "?YDNXax@P", "sjDZylk", "6goF", "ZofSvJE8p", "6|UdTVw"])

design=[_tlmBMqKyTQpk]
crossing=[_tlmBMqKyTQpk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_1_1"))

### END
