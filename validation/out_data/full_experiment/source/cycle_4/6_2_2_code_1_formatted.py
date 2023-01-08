### REGULAR FACTORS
zzikcb = Factor("zzikcb", ["vqfk", "agw"])
vwx = Factor("vwx", ["mgm", "ujhniq"])
wowvt = Factor("wowvt", ["vqfk", "agw"])
vwq = Factor("vwq", ["mgm", "ujhniq"])
fchnpa = Factor("fchnpa", ["cbk", "gvdxnm"])
eiznef = Factor("eiznef", ["trjw", "oerf"])
### DERIVED FACTORS
##
def sibk (wowvt, zzikcb):
    return wowvt == zzikcb
def bvlpxh (wowvt, zzikcb):
    return not sibk(wowvt, zzikcb)
smr = Factor("smr", [DerivedLevel("izh", WithinTrial(sibk, [wowvt, zzikcb])), DerivedLevel("clwvo", WithinTrial(bvlpxh, [wowvt, zzikcb]))])
##
def nop (vwx, eiznef):
    return vwx == eiznef
def ivd (vwx, eiznef):
    return not nop(vwx, eiznef)
ulkwbd = Factor("ulkwbd", [DerivedLevel("cvnh", WithinTrial(nop, [vwx, eiznef])), DerivedLevel("ysbpo", WithinTrial(ivd, [vwx, eiznef]))])
### EXPERIMENT
design=[smr,ulkwbd,zzikcb,vwx,wowvt,vwq,fchnpa,eiznef]
constraints=[AtLeastKInARow(2, vwx),AtMostKInARow(2, eiznef)]
crossing=[vwx,zzikcb]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
