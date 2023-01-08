### REGULAR FACTORS
kpdmg = Factor("kpdmg", ["psclbm", "lij"])
olgh = Factor("olgh", ["qru", "lseg"])
ipxtj = Factor("ipxtj", ["psclbm", "lij"])
pdjwng = Factor("pdjwng", ["qru", "lseg"])
yuou = Factor("yuou", ["otpq", "zgqit"])
### DERIVED FACTORS
##
def is_uibycy_mdp(olgh, kpdmg):
    return olgh == kpdmg
def is_uibycy_kjvo(olgh, kpdmg):
    return not is_uibycy_mdp(olgh, kpdmg)
uibycy = Factor("uibycy", [DerivedLevel("mdp", WithinTrial(is_uibycy_mdp, [olgh, kpdmg])), DerivedLevel("kjvo", WithinTrial(is_uibycy_kjvo, [olgh, kpdmg]))])
##
def is_mpxrez_ncv(pdjwng, yuou):
    return pdjwng == yuou
def is_mpxrez_xygm(pdjwng, yuou):
    return not is_mpxrez_ncv(pdjwng, yuou)
mpxrez = Factor("mpxrez", [DerivedLevel("ncv", WithinTrial(is_mpxrez_ncv, [pdjwng, yuou])), DerivedLevel("xygm", WithinTrial(is_mpxrez_xygm, [pdjwng, yuou]))])
### EXPERIMENT
constraints = [AtLeastKInARow(4, (mpxrez, "ncv"))]
crossing = [olgh, uibycy]
design=[kpdmg,olgh,ipxtj,pdjwng,yuou,uibycy,mpxrez]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
