from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pveal = Factor("pveal", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
axewwo = Factor("axewwo", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
xwxcp = Factor("xwxcp", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
def tfk(pveal, xwxcp, axewwo):
     return pveal == xwxcp
def hkb(pveal, xwxcp, axewwo):
     return xwxcp != pveal and pveal == axewwo
def pcrh(pveal, xwxcp, axewwo):
     return (pveal != xwxcp) and (not pveal == axewwo)
mkscp = Factor("ipe", [DerivedLevel("aopz", WithinTrial(tfk, [pveal, axewwo, xwxcp])), DerivedLevel("abbfb", WithinTrial(hkb, [pveal, axewwo, xwxcp])),DerivedLevel("pcwrkd", WithinTrial(pcrh, [pveal, axewwo, xwxcp]))])
### EXPERIMENT
design=[pveal,axewwo,xwxcp,mkscp]
crossing=[mkscp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END