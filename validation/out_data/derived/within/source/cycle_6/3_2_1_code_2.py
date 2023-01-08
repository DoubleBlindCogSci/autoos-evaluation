from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
clbqjx = Factor("clbqjx", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
axqomn = Factor("axqomn", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
ggxdbw = Factor("ggxdbw", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
def is_rhpg_hvsnph(clbqjx, axqomn, ggxdbw):
    return axqomn == clbqjx
def is_rhpg_qmkj(clbqjx, axqomn, ggxdbw):
    return axqomn != clbqjx and ggxdbw == clbqjx
def is_rhpg_jcsa(clbqjx, axqomn, ggxdbw):
    return not (is_rhpg_hvsnph(clbqjx, axqomn, ggxdbw) or is_rhpg_qmkj(clbqjx, axqomn, ggxdbw))
rhpg = Factor("rhpg", [DerivedLevel("hvsnph", WithinTrial(is_rhpg_hvsnph, [clbqjx, axqomn, ggxdbw])), DerivedLevel("qmkj", WithinTrial(is_rhpg_qmkj, [clbqjx, axqomn, ggxdbw])), DerivedLevel("jcsa", WithinTrial(is_rhpg_jcsa, [clbqjx, axqomn, ggxdbw]))])

design=[clbqjx,axqomn,ggxdbw,rhpg]
crossing=[rhpg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END