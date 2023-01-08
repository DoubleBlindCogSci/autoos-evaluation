from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ykil= Factor("ykil", ["wadw","qht","sdg","mjceo","wnh","dppk","etqf"])
ubblm= Factor("ubblm", ["wadw","qht","sdg","mjceo","wnh","dppk","etqf"])
xtiwp= Factor("xtiwp", ["wadw","qht","sdg","mjceo","wnh","dppk","etqf"])

def is_xoygyh_cflzf(ykil, xtiwp, ubblm):
    return ykil != xtiwp and ykil == ubblm
def is_xoygyh_gys(ykil, xtiwp, ubblm):
    return not is_xoygyh_cflzf(ykil, xtiwp, ubblm)
xoygyh= Factor("xoygyh", [DerivedLevel("cflzf", WithinTrial(is_xoygyh_cflzf, [ykil, xtiwp, ubblm])), DerivedLevel("gys", WithinTrial(is_xoygyh_gys, [ykil, xtiwp, ubblm]))])


design=[ykil,ubblm,xtiwp,xoygyh]
crossing=[xoygyh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
