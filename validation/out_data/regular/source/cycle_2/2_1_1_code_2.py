from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
S_oqGmtcgyXoaQ = Factor("S8oqGmtcgyXoaQ", [Level("iUyjqN}pxkc@& ", 1), Level("J[r", 3)])

design=[S_oqGmtcgyXoaQ]
crossing=[S_oqGmtcgyXoaQ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
