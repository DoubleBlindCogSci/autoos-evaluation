from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bvtzbp = Factor("bvtzbp", ["rst","bwcyv","rni","rszxy","cqo","zdqj","dbyspg"])
ylmywb = Factor("ylmywb", ["wviclj","cyan","zxqip","fhahdx","wzhfp"])
def uptknt(bvtzbp, ylmywb):
    return bvtzbp[-2] == "zdqj" and ylmywb[-1] != "wviclj"
def wvqu(bvtzbp,ylmywb):
    return not uptknt(bvtzbp, ylmywb)
eley = Factor("xbgs", [DerivedLevel("lxs", Window(uptknt, [bvtzbp, ylmywb],3,1)), DerivedLevel("gpjys", Window(wvqu, [bvtzbp, ylmywb],3,1))])
### EXPERIMENT
design=[bvtzbp,ylmywb,eley]
crossing=[eley]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END