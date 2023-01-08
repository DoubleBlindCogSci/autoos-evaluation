from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
rzazt = Factor("rzazt", ["yfjy", "qcomsb"])
mfxmh = Factor("mfxmh", ["njui", "kbdq"])
lejbn = Factor("lejbn", ["yfjy", "qcomsb"])
yseb = Factor("yseb", ["njui", "kbdq"])
skpifo = Factor("skpifo", ["syy", "pvbing"])
dfaag = Factor("dfaag", ["mtd", "zma"])
def awnll (dfaag, mfxmh):
    return dfaag == mfxmh
def lelm (dfaag, mfxmh):
    return not awnll(dfaag, mfxmh)
yrx = Factor("yrx", [DerivedLevel("uam", WithinTrial(awnll, [dfaag, mfxmh])), DerivedLevel("pbcmbd", WithinTrial(lelm, [dfaag, mfxmh]))])
def iqt (yseb, lejbn):
    return yseb == lejbn
def kxjuu (yseb, lejbn):
    return not iqt(yseb, lejbn)
sgguq = Factor("sgguq", [DerivedLevel("zsknwg", WithinTrial(iqt, [yseb, lejbn])), DerivedLevel("xua", WithinTrial(kxjuu, [yseb, lejbn]))])
design=[yrx,sgguq,rzazt,mfxmh,lejbn,yseb,skpifo,dfaag]
constraints=[MinimumTrials(46),AtMostKInARow(3, dfaag)]
crossing=[lejbn,yseb]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_2_2"))
