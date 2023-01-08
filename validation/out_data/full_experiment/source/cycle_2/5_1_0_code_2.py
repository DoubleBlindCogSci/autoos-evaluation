from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
dtr = Factor("dtr", ["ted", "rqhh"])
wlgsw = Factor("wlgsw", ["pbvh", "zkbz"])
pfj = Factor("pfj", ["ted", "rqhh"])
hbkma = Factor("hbkma", ["pbvh", "zkbz"])
lhe = Factor("lhe", ["dihh", "fpmzkq"])
def is_sovpx_xfxluk(dtr, pfj):
    return dtr == pfj
def is_sovpx_qmrrzn(dtr, pfj):
    return not is_sovpx_xfxluk(dtr, pfj)
sovpx= Factor("sovpx", [DerivedLevel("xfxluk", WithinTrial(is_sovpx_xfxluk, [dtr, pfj])), DerivedLevel("qmrrzn", WithinTrial(is_sovpx_qmrrzn, [dtr, pfj]))])
constraints = []
crossing = [wlgsw, sovpx]

design=[dtr,wlgsw,pfj,hbkma,lhe,sovpx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))
