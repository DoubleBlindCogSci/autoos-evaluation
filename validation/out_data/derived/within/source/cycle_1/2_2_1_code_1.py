from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ykil = Factor("ykil", ["wadw","qht","sdg","mjceo","wnh","dppk","etqf"])
ubblm = Factor("ubblm", ["wadw","qht","sdg","mjceo","wnh","dppk","etqf"])
xtiwp = Factor("xtiwp", ["wadw","qht","sdg","mjceo","wnh","dppk","etqf"])
def mbzwye(ykil, xtiwp, ubblm):
    return ykil != xtiwp and ykil == ubblm
def xvul(ykil, xtiwp, ubblm):
    return not (ykil != xtiwp) or ykil != ubblm
ymzkmp = DerivedLevel("cflzf", WithinTrial(mbzwye, [ykil, ubblm, xtiwp]))
xjk = DerivedLevel("gys", WithinTrial(xvul, [ykil, ubblm, xtiwp]))
grgag = Factor("xoygyh", [ymzkmp, xjk])

### EXPERIMENT
design=[ykil,ubblm,xtiwp,grgag]
crossing=[grgag]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END