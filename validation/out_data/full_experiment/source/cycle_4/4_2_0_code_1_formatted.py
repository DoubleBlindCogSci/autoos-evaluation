### REGULAR FACTORS
npfih = Factor("npfih", ["zqc", "szrkc"])
ldtn = Factor("ldtn", ["eqq", "mcuj"])
olhm = Factor("olhm", ["zqc", "szrkc"])
vac = Factor("vac", ["eqq", "mcuj"])
### DERIVED FACTORS
##
def tuqne (olhm, npfih):
    return olhm == npfih
def lopnc (olhm, npfih):
    return not tuqne(olhm, npfih)
rnm = Factor("rnm", [DerivedLevel("zsrr", WithinTrial(tuqne, [olhm, npfih])), DerivedLevel("ebnz", WithinTrial(lopnc, [olhm, npfih]))])
##
def eofmvl (vac, ldtn):
    return vac == ldtn
def vxcr (vac, ldtn):
    return not eofmvl(vac, ldtn)
oelqby = Factor("oelqby", [DerivedLevel("njfk", WithinTrial(eofmvl, [vac, ldtn])), DerivedLevel("oaiui", WithinTrial(vxcr, [vac, ldtn]))])
### EXPERIMENT
design=[rnm,oelqby,npfih,ldtn,olhm,vac]
constraints=[]
crossing=[ldtn,olhm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
