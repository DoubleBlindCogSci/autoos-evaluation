from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wFEZE_WUQ_t = Factor("wFEZE#WUQ^t", [Level("S9Gz", 9), "]uxfmS3bj}6e8J", "ryhLbZLomRXrRH", "S1UcMomU_r", Level("upmMsKYZ62P", 1), "WXXP", "dsQ7ezis~j"])
QfmIuVqDqzptL = Factor("QfmIuVqDqzptL", ["2URpZLt", Level("L7eW79tbVind", 4), Level("gCXjuKd7EvLFDA", 1), "9zTxCzUQSQd#q", "EEMHqfpV]", "EgKs)uVRZmNws", "FanE", "sN4tdjli]"])

design=[wFEZE_WUQ_t,QfmIuVqDqzptL]
crossing=[wFEZE_WUQ_t,QfmIuVqDqzptL]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_0"))

### END
