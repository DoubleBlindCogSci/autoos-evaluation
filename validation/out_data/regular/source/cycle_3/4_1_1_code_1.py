from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
i2LnESDU3yZ=[Level("oGwkbvwv2Y",7),Level("zfD",4),"lAd",Level("VRRkSzB2ShWhng",4)]
hJxWX2NiY9=Factor("bG*eJ%xLr",i2LnESDU3yZ)

### EXPERIMENT
design=[hJxWX2NiY9]
crossing=[hJxWX2NiY9]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
### END