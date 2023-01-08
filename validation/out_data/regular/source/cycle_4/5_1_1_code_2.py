from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
N_ZbQYw = Factor("N_ZbQYw",  ["om&vC", "wLF", "iTb", "FOx1eN", "MtJ", Level("pWE", 1)])

design=[N_ZbQYw]
crossing=[N_ZbQYw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_1"))

### END
