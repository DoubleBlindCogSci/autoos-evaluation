from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
k_ao_PgTEM = Factor("k%ao PgTEM", ["EftQj}iZ", Level("*hY^VVAWMpGB", 1)])

design=[k_ao_PgTEM]
crossing=[k_ao_PgTEM]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
