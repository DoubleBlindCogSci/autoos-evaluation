from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bG_eJ_xLr = Factor("bG*eJ%xLr", [Level("oGwkbvwv2Y", 7), Level("zfD", 1), Level("lAd", 1), Level("VRRkSzB2ShWhng", 4)])

design=[bG_eJ_xLr]
crossing=[bG_eJ_xLr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))

### END
