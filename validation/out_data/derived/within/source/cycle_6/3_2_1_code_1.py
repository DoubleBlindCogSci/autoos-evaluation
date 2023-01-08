from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
clbqjx = Factor("clbqjx", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
axqomn = Factor("axqomn", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
ggxdbw = Factor("ggxdbw", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
def yztmtc(clbqjx, axqomn, ggxdbw):
     return axqomn == clbqjx
def jylgrl(clbqjx, axqomn, ggxdbw):
     return axqomn != clbqjx and ggxdbw == clbqjx
def xiry(clbqjx, axqomn, ggxdbw):
     return (not clbqjx == axqomn) and (not jylgrl(clbqjx, axqomn, ggxdbw))
txoa = Factor("rhpg", [DerivedLevel("hvsnph", WithinTrial(yztmtc, [clbqjx, axqomn, ggxdbw])), DerivedLevel("qmkj", WithinTrial(jylgrl, [clbqjx, axqomn, ggxdbw])),DerivedLevel("jcsa", WithinTrial(xiry, [clbqjx, axqomn, ggxdbw]))])
### EXPERIMENT
design=[clbqjx,axqomn,ggxdbw,txoa]
crossing=[txoa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END