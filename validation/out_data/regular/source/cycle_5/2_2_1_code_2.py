from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ihj = Factor("Ihj", ["SZcP$q7T3E4Xkt", "q4(peIyBCDBe"])
mNPT__Lq_x_ = Factor("mNPT[!Lq2x~", ["aPoSYR2ehnve", "BSF"])

design=[Ihj,mNPT__Lq_x_]
crossing=[Ihj,mNPT__Lq_x_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
