from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
rzazt = Factor("rzazt", ["yfjy", "qcomsb"])
mfxmh = Factor("mfxmh", ["njui", "kbdq"])
lejbn = Factor("lejbn", ["yfjy", "qcomsb"])
yseb = Factor("yseb", ["njui", "kbdq"])
skpifo = Factor("skpifo", ["syy", "pvbing"])
dfaag = Factor("dfaag", ["mtd", "zma"])
def is_yrx_uam(dfaag, mfxmh):
    return dfaag == mfxmh
def is_yrx_pbcmbd(dfaag, mfxmh):
    return not is_yrx_uam(dfaag, mfxmh)
yrx= Factor("yrx", [DerivedLevel("uam", WithinTrial(is_yrx_uam, [dfaag, mfxmh])), DerivedLevel("pbcmbd", WithinTrial(is_yrx_pbcmbd, [dfaag, mfxmh]))])
def is_sgguq_zsknwg(yseb, lejbn):
    return yseb == lejbn
def is_sgguq_xua(yseb, lejbn):
    return not is_sgguq_zsknwg(yseb, lejbn)
sgguq= Factor("sgguq", [DerivedLevel("zsknwg", WithinTrial(is_sgguq_zsknwg, [yseb, lejbn])), DerivedLevel("xua", WithinTrial(is_sgguq_xua, [yseb, lejbn]))])
constraints = [AtMostKInARow(3, dfaag), MinimumTrials(46)]
crossing = [lejbn, yseb]

design=[rzazt,mfxmh,lejbn,yseb,skpifo,dfaag]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_2_2"))
