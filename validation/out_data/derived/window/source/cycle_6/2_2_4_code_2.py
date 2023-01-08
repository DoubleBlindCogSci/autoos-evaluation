from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bvtzbp = Factor("bvtzbp", ["rst","bwcyv","rni","rszxy","cqo","zdqj","dbyspg"])
ylmywb = Factor("ylmywb", ["wviclj","cyan","zxqip","fhahdx","wzhfp"])
def is_xbgs_lxs(bvtzbp, ylmywb):
    return bvtzbp[-2] == "zdqj" and ylmywb[-1] != "wviclj"
def is_xbgs_gpjys(bvtzbp, ylmywb):
    return not is_xbgs_lxs(bvtzbp, ylmywb)
xbgs = Factor("xbgs", [DerivedLevel("lxs", Window(is_xbgs_lxs, [bvtzbp, ylmywb], 3, 1)), DerivedLevel("gpjys", Window(is_xbgs_gpjys, [bvtzbp, ylmywb], 3, 1))])

design=[bvtzbp,ylmywb,xbgs]
crossing=[xbgs]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END