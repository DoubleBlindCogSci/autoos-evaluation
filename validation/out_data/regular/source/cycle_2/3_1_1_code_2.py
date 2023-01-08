from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ouOm = Factor("ouOm", ["oLXg1ht", "1efKq8Up[Yi*s", "p9d&M H"])

design=[ouOm]
crossing=[ouOm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
