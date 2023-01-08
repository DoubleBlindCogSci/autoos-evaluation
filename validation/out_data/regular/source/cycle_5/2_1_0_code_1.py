from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uX4l7xNZ6="Wmqs&B7"
LL6yt=['RWvqo;',"KqJ",uX4l7xNZ6]
eCwH=Factor("!ENoPJmsgqV",LL6yt)

### EXPERIMENT
design=[eCwH]
crossing=[eCwH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END