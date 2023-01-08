from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ymlq = Factor("ymlq", ["alar","bdc","hjo","jdgw","ghuu"])
zwwp = Factor("zwwp", ["alar","bdc","hjo","jdgw","ghuu"])
ttm = Factor("ttm", ["alar","bdc","hjo","jdgw","ghuu"])
def koki(ymlq, zwwp, ttm):
    return ymlq == zwwp and ymlq != ttm
def njfk(ymlq, zwwp, ttm):
    return ymlq != zwwp or not (ymlq != ttm)
lguey = DerivedLevel("nds", WithinTrial(koki, [ymlq, zwwp, ttm]))
murqaw = DerivedLevel("ttcxl", WithinTrial(njfk, [ymlq, zwwp, ttm]))
iorztm = Factor("ksxz", [lguey, murqaw])

### EXPERIMENT
design=[ymlq,zwwp,ttm,iorztm]
crossing=[iorztm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END