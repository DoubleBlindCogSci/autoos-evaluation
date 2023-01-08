from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
nzn = Factor("nzn", ["nvvtv", "patw"])
slm = Factor("slm", ["boga", "flif"])
qaufq = Factor("qaufq", ["nvvtv", "patw"])
uzqpl = Factor("uzqpl", ["boga", "flif"])
def uqx (slm, qaufq):
    return slm == qaufq
def ygekhj (slm, qaufq):
    return not uqx(slm, qaufq)
ehzalf = Factor("ehzalf", [DerivedLevel("bsigle", WithinTrial(uqx, [slm, qaufq])), DerivedLevel("hbc", WithinTrial(ygekhj, [slm, qaufq]))])
def xjekg (uzqpl, nzn):
    return uzqpl == nzn
def pvfxh (uzqpl, nzn):
    return not xjekg(uzqpl, nzn)
jxh = Factor("jxh", [DerivedLevel("safm", WithinTrial(xjekg, [uzqpl, nzn])), DerivedLevel("byfhj", WithinTrial(pvfxh, [uzqpl, nzn]))])
design=[ehzalf,jxh,nzn,slm,qaufq,uzqpl]
constraints=[AtLeastKInARow(4, qaufq),MinimumTrials(15)]
crossing=[jxh,ehzalf]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_2"))
