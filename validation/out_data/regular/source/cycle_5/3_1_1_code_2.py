from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
SYp_IZBjSz = Factor("SYp|IZBjSz", ["2hM", "#U1QiJe", "P]yVBDrT"])

design=[SYp_IZBjSz]
crossing=[SYp_IZBjSz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
