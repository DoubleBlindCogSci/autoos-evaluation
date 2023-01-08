from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
zzikcb = Factor("zzikcb", ["vqfk", "agw"])
vwx = Factor("vwx", ["mgm", "ujhniq"])
wowvt = Factor("wowvt", ["vqfk", "agw"])
vwq = Factor("vwq", ["mgm", "ujhniq"])
fchnpa = Factor("fchnpa", ["cbk", "gvdxnm"])
eiznef = Factor("eiznef", ["trjw", "oerf"])
def is_smr_izh(wowvt, zzikcb):
    return wowvt == zzikcb
def is_smr_clwvo(wowvt, zzikcb):
    return not is_smr_izh(wowvt, zzikcb)
smr = Factor("smr", [DerivedLevel("izh", WithinTrial(is_smr_izh, [wowvt, zzikcb])), DerivedLevel("clwvo", WithinTrial(is_smr_clwvo, [wowvt, zzikcb]))])
def is_ulkwbd_cvnh(vwx, eiznef):
    return vwx == eiznef
def is_ulkwbd_ysbpo(vwx, eiznef):
    return not is_ulkwbd_cvnh(vwx, eiznef)
ulkwbd = Factor("ulkwbd", [DerivedLevel("cvnh", WithinTrial(is_ulkwbd_cvnh, [vwx, eiznef])), DerivedLevel("ysbpo", WithinTrial(is_ulkwbd_ysbpo, [vwx, eiznef]))])
constraints = [AtLeastKInARow(2, vwx), AtMostKInARow(2, eiznef)]
crossing = [vwx, zzikcb]

design=[zzikcb,vwx,wowvt,vwq,fchnpa,eiznef,smr,ulkwbd]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_2"))
