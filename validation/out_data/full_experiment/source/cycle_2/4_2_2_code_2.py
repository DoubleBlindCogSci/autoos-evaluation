from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
nzn = Factor("nzn", ["nvvtv", "patw"])
slm = Factor("slm", ["boga", "flif"])
qaufq = Factor("qaufq", ["nvvtv", "patw"])
uzqpl = Factor("uzqpl", ["boga", "flif"])
def is_ehzalf_bsigle(slm, qaufq):
    return slm == qaufq
def is_ehzalf_hbc(slm, qaufq):
    return not is_ehzalf_bsigle(slm, qaufq)
ehzalf= Factor("ehzalf", [DerivedLevel("bsigle", WithinTrial(is_ehzalf_bsigle, [slm, qaufq])), DerivedLevel("hbc", WithinTrial(is_ehzalf_hbc, [slm, qaufq]))])
def is_jxh_safm(uzqpl, nzn):
    return uzqpl == nzn
def is_jxh_byfhj(uzqpl, nzn):
    return not is_jxh_safm(uzqpl, nzn)
jxh= Factor("jxh", [DerivedLevel("safm", WithinTrial(is_jxh_safm, [uzqpl, nzn])), DerivedLevel("byfhj", WithinTrial(is_jxh_byfhj, [uzqpl, nzn]))])
constraints = [AtLeastKInARow(4, (qaufq, "patw")), MinimumTrials(15)]
crossing = [jxh, ehzalf]

design=[nzn,slm,qaufq,uzqpl,ehzalf,jxh]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_2"))
