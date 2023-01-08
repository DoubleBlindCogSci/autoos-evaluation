from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_ENoPJmsgqV = Factor("!ENoPJmsgqV", ["RWvqo;", "KqJ", "Wmqs&B7"])


design=[_ENoPJmsgqV]
crossing=[_ENoPJmsgqV]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
