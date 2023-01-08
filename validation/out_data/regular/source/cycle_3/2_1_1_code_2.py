from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bdYlua = Factor("bdYlua", [Level("Qdn", 9), Level("SO ]FKkH", 1)])

design=[bdYlua]
crossing=[bdYlua]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
