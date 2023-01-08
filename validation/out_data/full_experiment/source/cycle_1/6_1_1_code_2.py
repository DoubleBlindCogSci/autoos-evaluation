from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
gqw = Factor("gqw", ["ohpe", "rbclng"])
wdp = Factor("wdp", ["eioqw", "rrvin"])
nrbavq = Factor("nrbavq", ["ohpe", "rbclng"])
xlpll = Factor("xlpll", ["eioqw", "rrvin"])
xne = Factor("xne", ["erjk", "yow"])
cee = Factor("cee", ["yqzavs", "gof"])
def is_zzsf_cmjwd(nrbavq, wdp):
    return nrbavq == wdp
def is_zzsf_yffeb(nrbavq, wdp):
    return not is_zzsf_cmjwd(nrbavq, wdp)
zzsf= Factor("zzsf", [DerivedLevel("cmjwd", WithinTrial(is_zzsf_cmjwd, [nrbavq, wdp])), DerivedLevel("yffeb", WithinTrial(is_zzsf_yffeb, [nrbavq, wdp]))])
constraints = [MinimumTrials(39)]
crossing = [nrbavq, cee]

design=[gqw,wdp,nrbavq,xlpll,xne,cee]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_1_1"))
