### REGULAR FACTORS
npfih = Factor("npfih", ["zqc", "szrkc"])
ldtn = Factor("ldtn", ["eqq", "mcuj"])
olhm = Factor("olhm", ["zqc", "szrkc"])
vac = Factor("vac", ["eqq", "mcuj"])
### DERIVED FACTORS
##
def is_rnm_zsrr(olhm, npfih):
    return olhm == npfih
def is_rnm_ebnz(olhm, npfih):
    return not is_rnm_zsrr(olhm, npfih)
rnm = Factor("rnm", [DerivedLevel("zsrr", WithinTrial(is_rnm_zsrr, [olhm, npfih])), DerivedLevel("ebnz", WithinTrial(is_rnm_ebnz, [olhm, npfih]))])
##
def is_oelqby_njfk(vac, ldtn):
    return vac == ldtn
def is_oelqby_oaiui(vac, ldtn):
    return not is_oelqby_njfk(vac, ldtn)
oelqby = Factor("oelqby", [DerivedLevel("njfk", WithinTrial(is_oelqby_njfk, [vac, ldtn])), DerivedLevel("oaiui", WithinTrial(is_oelqby_oaiui, [vac, ldtn]))])
### EXPERIMENT
constraints = []
crossing = [ldtn, olhm]
design=[npfih,ldtn,olhm,vac,rnm,oelqby]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
