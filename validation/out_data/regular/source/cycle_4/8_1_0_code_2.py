from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zXOQ = Factor("zXOQ", ["tHf<Fxy", "CaQdo", "vrTWiae{", "htf", "yuWaJJe:O", "UPddbk", "2Iincw", " dR(sP"])

design=[zXOQ]
crossing=[zXOQ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_0"))

### END
