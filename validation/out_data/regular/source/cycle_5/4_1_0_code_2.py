from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_sXyFTqTfX = Factor("[sXyFTqTfX",  ["A&DJHpbpIV6C", "Dy", "L<0fbyXbsHS", Level("%XXtRH!Y", 4)])


design=[_sXyFTqTfX]
crossing=[_sXyFTqTfX]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_0"))

### END
