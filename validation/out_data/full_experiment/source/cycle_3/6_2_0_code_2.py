from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
uirvdf = Factor("uirvdf", ["ljjzo", "vmds"])
skcfby = Factor("skcfby", ["bwls", "jbj"])
imowog = Factor("imowog", ["ljjzo", "vmds"])
lwou = Factor("lwou", ["bwls", "jbj"])
sws = Factor("sws", ["pewpg", "jniby"])
wfhvd = Factor("wfhvd", ["pmjf", "xrzjqz"])
def is_fdp_rufmz(imowog, wfhvd):
    return imowog == wfhvd
def is_fdp_ssrvcv(imowog, wfhvd):
    return not is_fdp_rufmz(imowog, wfhvd)
fdp = Factor("fdp", [DerivedLevel("rufmz", WithinTrial(is_fdp_rufmz, [imowog, wfhvd])), DerivedLevel("ssrvcv", WithinTrial(is_fdp_ssrvcv, [imowog, wfhvd]))])
def is_xwpnof_wqvxe(skcfby, uirvdf):
    return skcfby == uirvdf
def is_xwpnof_zbc(skcfby, uirvdf):
    return not is_xwpnof_wqvxe(skcfby, uirvdf)
xwpnof = Factor("xwpnof", [DerivedLevel("wqvxe", WithinTrial(is_xwpnof_wqvxe, [skcfby, uirvdf])), DerivedLevel("zbc", WithinTrial(is_xwpnof_zbc, [skcfby, uirvdf]))])
constraints = []
crossing = [wfhvd, sws]

design=[uirvdf,skcfby,imowog,lwou,sws,wfhvd,fdp,xwpnof]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_0"))
