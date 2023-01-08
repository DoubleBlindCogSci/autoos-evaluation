### REGULAR FACTORS
uirvdf = Factor("uirvdf", ["ljjzo", "vmds"])
skcfby = Factor("skcfby", ["bwls", "jbj"])
imowog = Factor("imowog", ["ljjzo", "vmds"])
lwou = Factor("lwou", ["bwls", "jbj"])
sws = Factor("sws", ["pewpg", "jniby"])
wfhvd = Factor("wfhvd", ["pmjf", "xrzjqz"])
### DERIVED FACTORS
##
def ymjp (imowog, wfhvd):
    return imowog == wfhvd
def xodrv (imowog, wfhvd):
    return not ymjp(imowog, wfhvd)
fdp = Factor("fdp", [DerivedLevel("rufmz", WithinTrial(ymjp, [imowog, wfhvd])), DerivedLevel("ssrvcv", WithinTrial(xodrv, [imowog, wfhvd]))])
##
def egvhq (skcfby, uirvdf):
    return skcfby == uirvdf
def mns (skcfby, uirvdf):
    return not egvhq(skcfby, uirvdf)
xwpnof = Factor("xwpnof", [DerivedLevel("wqvxe", WithinTrial(egvhq, [skcfby, uirvdf])), DerivedLevel("zbc", WithinTrial(mns, [skcfby, uirvdf]))])
### EXPERIMENT
design=[fdp,xwpnof,uirvdf,skcfby,imowog,lwou,sws,wfhvd]
constraints=[]
crossing=[wfhvd,sws]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
