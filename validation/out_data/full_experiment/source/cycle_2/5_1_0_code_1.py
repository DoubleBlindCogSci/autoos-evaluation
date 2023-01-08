from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
dtr = Factor("dtr", ["ted", "rqhh"])
wlgsw = Factor("wlgsw", ["pbvh", "zkbz"])
pfj = Factor("pfj", ["ted", "rqhh"])
hbkma = Factor("hbkma", ["pbvh", "zkbz"])
lhe = Factor("lhe", ["dihh", "fpmzkq"])
def ywhf (dtr, pfj):
    return dtr == pfj
def irebb (dtr, pfj):
    return not ywhf(dtr, pfj)
sovpx = Factor("sovpx", [DerivedLevel("xfxluk", WithinTrial(ywhf, [dtr, pfj])), DerivedLevel("qmrrzn", WithinTrial(irebb, [dtr, pfj]))])
design=[sovpx,dtr,wlgsw,pfj,hbkma,lhe]
constraints=[]
crossing=[wlgsw,sovpx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
