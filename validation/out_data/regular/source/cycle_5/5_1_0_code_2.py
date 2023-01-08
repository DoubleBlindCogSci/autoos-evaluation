from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EFHQ_k = Factor("EFHQ)k",  [Level("oqeT|tJS<WSSEC", 3), "oKrDKC", "BKfUXaJFxB|L", "!y1GToHDk", "RBKNY)uvHVFAm"])

design=[EFHQ_k]
crossing=[EFHQ_k]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))

### END
