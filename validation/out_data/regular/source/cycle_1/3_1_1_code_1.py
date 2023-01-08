from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
PQtkJAd_C2Q=[Level("M5f YwhvoB6Up",2),'v}Q',"$vFDzKwzEwVMU"]
N99ft=Factor('yzVj[%cdkx',PQtkJAd_C2Q)

### EXPERIMENT
design=[N99ft]
crossing=[N99ft]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/3_1_1"))
### END