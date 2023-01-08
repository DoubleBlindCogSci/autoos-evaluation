from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uIV6dBM=["qVsT",':Pi14o!ZLjKM',"wLF"]
qSiJ=Factor('N_ZbQYw',["om&vC",uIV6dBM[2],'iTb',"FOx1eN",'MtJ',Level("pWE",1)])

### EXPERIMENT
design=[qSiJ]
crossing=[qSiJ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
### END