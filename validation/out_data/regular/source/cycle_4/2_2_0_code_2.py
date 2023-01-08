from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TYMlTtvTpAn_ = Factor("TYMlTtvTpAn6", ["A&eqHLdg", "ubIxn#B"])
hkRCuBJ_ = Factor("hkRCuBJ7", ["I<uQ", "*BCeDY#mQzccC"])

design=[TYMlTtvTpAn_,hkRCuBJ_]
crossing=[TYMlTtvTpAn_,hkRCuBJ_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
