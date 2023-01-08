from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
kpdmg = Factor("kpdmg", ["psclbm", "lij"])
olgh = Factor("olgh", ["qru", "lseg"])
ipxtj = Factor("ipxtj", ["psclbm", "lij"])
pdjwng = Factor("pdjwng", ["qru", "lseg"])
yuou = Factor("yuou", ["otpq", "zgqit"])
def ftkodo (olgh, kpdmg):
    return olgh == kpdmg
def vzdhzl (olgh, kpdmg):
    return not ftkodo(olgh, kpdmg)
uibycy = Factor("uibycy", [DerivedLevel("mdp", WithinTrial(ftkodo, [olgh, kpdmg])), DerivedLevel("kjvo", WithinTrial(vzdhzl, [olgh, kpdmg]))])
def vazie (pdjwng, yuou):
    return pdjwng == yuou
def yqyyqi (pdjwng, yuou):
    return not vazie(pdjwng, yuou)
mpxrez = Factor("mpxrez", [DerivedLevel("ncv", WithinTrial(vazie, [pdjwng, yuou])), DerivedLevel("xygm", WithinTrial(yqyyqi, [pdjwng, yuou]))])
design=[uibycy,mpxrez,kpdmg,olgh,ipxtj,pdjwng,yuou]
constraints=[AtLeastKInARow(4, ipxtj)]
crossing=[olgh,uibycy]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
