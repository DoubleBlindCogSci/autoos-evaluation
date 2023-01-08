from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
uirvdf = Factor("uirvdf", ["ljjzo", "vmds"])
skcfby = Factor("skcfby", ["bwls", "jbj"])
imowog = Factor("imowog", ["ljjzo", "vmds"])
lwou = Factor("lwou", ["bwls", "jbj"])
sws = Factor("sws", ["pewpg", "jniby"])
wfhvd = Factor("wfhvd", ["pmjf", "xrzjqz"])
def ymjp (imowog, wfhvd):
    return imowog == wfhvd
def xodrv (imowog, wfhvd):
    return not ymjp(imowog, wfhvd)
fdp = Factor("fdp", [DerivedLevel("rufmz", WithinTrial(ymjp, [imowog, wfhvd])), DerivedLevel("ssrvcv", WithinTrial(xodrv, [imowog, wfhvd]))])
def egvhq (skcfby, uirvdf):
    return skcfby == uirvdf
def mns (skcfby, uirvdf):
    return not egvhq(skcfby, uirvdf)
xwpnof = Factor("xwpnof", [DerivedLevel("wqvxe", WithinTrial(egvhq, [skcfby, uirvdf])), DerivedLevel("zbc", WithinTrial(mns, [skcfby, uirvdf]))])
design=[fdp,xwpnof,uirvdf,skcfby,imowog,lwou,sws,wfhvd]
constraints=[]
crossing=[wfhvd,sws]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
