from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xTOwUCLvJCZYec = Factor("xTOwUCLvJCZYec", ["MckQxHCIqKTMh", "auQp"])
EF_p__FYX = Factor("EF<p|&FYX", ["JBT{xb", "dvdy}&ZA"])
IF_njruktyV = Factor("IF}njruktyV", ["RkpdX", "vx?B"])

design=[xTOwUCLvJCZYec,EF_p__FYX,IF_njruktyV]
crossing=[xTOwUCLvJCZYec,EF_p__FYX,IF_njruktyV]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_1"))

### END
