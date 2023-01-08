from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
gqw = Factor("gqw", ["ohpe", "rbclng"])
wdp = Factor("wdp", ["eioqw", "rrvin"])
nrbavq = Factor("nrbavq", ["ohpe", "rbclng"])
xlpll = Factor("xlpll", ["eioqw", "rrvin"])
xne = Factor("xne", ["erjk", "yow"])
cee = Factor("cee", ["yqzavs", "gof"])
def rofz (nrbavq, wdp):
    return nrbavq == wdp
def yfsv (nrbavq, wdp):
    return not rofz(nrbavq, wdp)
zzsf = Factor("zzsf", [DerivedLevel("cmjwd", WithinTrial(rofz, [nrbavq, wdp])), DerivedLevel("yffeb", WithinTrial(yfsv, [nrbavq, wdp]))])
design=[zzsf,gqw,wdp,nrbavq,xlpll,xne,cee]
constraints=[MinimumTrials(39)]
crossing=[nrbavq,cee]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_1_1"))
