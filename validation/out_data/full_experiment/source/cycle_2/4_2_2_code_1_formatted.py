### REGULAR FACTORS
nzn = Factor("nzn", ["nvvtv", "patw"])
slm = Factor("slm", ["boga", "flif"])
qaufq = Factor("qaufq", ["nvvtv", "patw"])
uzqpl = Factor("uzqpl", ["boga", "flif"])
### DERIVED FACTORS
##
def uqx (slm, qaufq):
    return slm == qaufq
def ygekhj (slm, qaufq):
    return not uqx(slm, qaufq)
ehzalf = Factor("ehzalf", [DerivedLevel("bsigle", WithinTrial(uqx, [slm, qaufq])), DerivedLevel("hbc", WithinTrial(ygekhj, [slm, qaufq]))])
##
def xjekg (uzqpl, nzn):
    return uzqpl == nzn
def pvfxh (uzqpl, nzn):
    return not xjekg(uzqpl, nzn)
jxh = Factor("jxh", [DerivedLevel("safm", WithinTrial(xjekg, [uzqpl, nzn])), DerivedLevel("byfhj", WithinTrial(pvfxh, [uzqpl, nzn]))])
### EXPERIMENT
design=[ehzalf,jxh,nzn,slm,qaufq,uzqpl]
constraints=[AtLeastKInARow(4, qaufq),MinimumTrials(15)]
crossing=[jxh,ehzalf]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
