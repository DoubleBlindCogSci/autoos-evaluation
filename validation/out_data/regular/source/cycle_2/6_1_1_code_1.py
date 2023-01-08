from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DkVKNtsFGLs=['3bbnhcbE',Level(':NUysnqtG{iRn(',10),Level("bVTtnrnteksEr",6),'bzRkSJ',Level('ySkzbupsM',4),Level('fOS',3)]
SGifQ2aY4Vy=Factor("bKCN",DkVKNtsFGLs)

### EXPERIMENT
design=[SGifQ2aY4Vy]
crossing=[SGifQ2aY4Vy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_1"))
### END