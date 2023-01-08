from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
mhwfb = Factor("mhwfb", ["nqfkbi", "hvatw"])
xdpvuw = Factor("xdpvuw", ["xmkm", "mbz"])
jtlrt = Factor("jtlrt", ["nqfkbi", "hvatw"])
ior = Factor("ior", ["xmkm", "mbz"])
nhulxc = Factor("nhulxc", ["ffqhy", "ydycxv"])
def is_mps_yunbbk(xdpvuw, jtlrt):
    return xdpvuw == jtlrt
def is_mps_gpiev(xdpvuw, jtlrt):
    return not is_mps_yunbbk(xdpvuw, jtlrt)
mps = Factor("mps", [DerivedLevel("yunbbk", WithinTrial(is_mps_yunbbk, [xdpvuw, jtlrt])), DerivedLevel("gpiev", WithinTrial(is_mps_gpiev, [xdpvuw, jtlrt]))])
constraints = [AtMostKInARow(4, mhwfb), MinimumTrials(26)]
crossing = [xdpvuw, mps]

design=[mhwfb,xdpvuw,jtlrt,ior,nhulxc,mps]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_2"))
