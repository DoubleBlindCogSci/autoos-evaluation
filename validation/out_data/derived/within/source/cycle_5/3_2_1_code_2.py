from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pveal = Factor("pveal", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
axewwo = Factor("axewwo", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
xwxcp = Factor("xwxcp", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
def is_ipe_aopz(pveal, axewwo, xwxcp):
    return pveal == xwxcp
def is_ipe_abbfb(pveal, axewwo, xwxcp):
    return pveal != xwxcp and pveal == axewwo
def is_ipe_pcwrkd(pveal, axewwo, xwxcp):
    return pveal != xwxcp and pveal != axewwo
ipe = Factor("ipe", [DerivedLevel("aopz", WithinTrial(is_ipe_aopz, [pveal, axewwo, xwxcp])), DerivedLevel("abbfb", WithinTrial(is_ipe_abbfb, [pveal, axewwo, xwxcp])), DerivedLevel("pcwrkd", WithinTrial(is_ipe_pcwrkd, [pveal, axewwo, xwxcp]))])

design=[pveal,axewwo,xwxcp,ipe]
crossing=[ipe]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END