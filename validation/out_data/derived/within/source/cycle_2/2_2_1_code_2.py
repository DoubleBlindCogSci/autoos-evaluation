from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ymlq= Factor("ymlq", ["alar","bdc","hjo","jdgw","ghuu"])
zwwp= Factor("zwwp", ["alar","bdc","hjo","jdgw","ghuu"])
ttm= Factor("ttm", ["alar","bdc","hjo","jdgw","ghuu"])
def is_ksxz_nds(ymlq, zwwp, ttm):
    return ymlq == zwwp and ymlq != ttm
def is_ksxz_ttcxl(ymlq, zwwp, ttm):
    return not (is_ksxz_nds(ymlq, zwwp, ttm))
ksxz= Factor("ksxz", [DerivedLevel("nds", WithinTrial(is_ksxz_nds, [ymlq, zwwp, ttm])), DerivedLevel("ttcxl", WithinTrial(is_ksxz_ttcxl, [ymlq, zwwp, ttm]))])

design=[ymlq,zwwp,ttm, ksxz]
crossing=[ksxz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
