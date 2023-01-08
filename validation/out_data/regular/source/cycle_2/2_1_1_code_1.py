from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gpMxa=['iUyjqN}pxkc@& ',Level('J[r',3)]
qrTEm=Factor('S8oqGmtcgyXoaQ',gpMxa)

### EXPERIMENT
design=[qrTEm]
crossing=[qrTEm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END