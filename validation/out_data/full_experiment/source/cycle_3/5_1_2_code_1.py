from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
mhwfb = Factor("mhwfb", ["nqfkbi", "hvatw"])
xdpvuw = Factor("xdpvuw", ["xmkm", "mbz"])
jtlrt = Factor("jtlrt", ["nqfkbi", "hvatw"])
ior = Factor("ior", ["xmkm", "mbz"])
nhulxc = Factor("nhulxc", ["ffqhy", "ydycxv"])
def brpyxa (xdpvuw, jtlrt):
    return xdpvuw == jtlrt
def lfwe (xdpvuw, jtlrt):
    return not brpyxa(xdpvuw, jtlrt)
mps = Factor("mps", [DerivedLevel("yunbbk", WithinTrial(brpyxa, [xdpvuw, jtlrt])), DerivedLevel("gpiev", WithinTrial(lfwe, [xdpvuw, jtlrt]))])
design=[mps,mhwfb,xdpvuw,jtlrt,ior,nhulxc]
constraints=[MinimumTrials(26),AtMostKInARow(4, mhwfb)]
crossing=[xdpvuw,mps]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_2"))
