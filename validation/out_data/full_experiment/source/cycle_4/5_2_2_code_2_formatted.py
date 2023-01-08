### REGULAR FACTORS
ihaxo = Factor("ihaxo", ["nebj", "gqov"])
mwabx = Factor("mwabx", ["upfna", "qnn"])
drfsq = Factor("drfsq", ["nebj", "gqov"])
wwviw = Factor("wwviw", ["upfna", "qnn"])
ddx = Factor("ddx", ["oesdd", "cgcxdg"])
### DERIVED FACTORS
##
def is_mehm_onat(wwviw, ddx):
    return wwviw == ddx
def is_mehm_zbtzh(wwviw, ddx):
    return not is_mehm_onat(wwviw, ddx)
mehm = Factor("mehm", [DerivedLevel("onat", WithinTrial(is_mehm_onat, [wwviw, ddx])), DerivedLevel("zbtzh", WithinTrial(is_mehm_zbtzh, [wwviw, ddx]))])
##
def is_trtz_itvon(drfsq, ihaxo):
    return drfsq == ihaxo
def is_trtz_cuvewk(drfsq, ihaxo):
    return not is_trtz_itvon(drfsq, ihaxo)
trtz = Factor("trtz", [DerivedLevel("itvon", WithinTrial(is_trtz_itvon, [drfsq, ihaxo])), DerivedLevel("cuvewk", WithinTrial(is_trtz_cuvewk, [drfsq, ihaxo]))])
### EXPERIMENT
constraints = [ExactlyK(3, (trtz, "cuvewk")), AtLeastKInARow(2, (trtz, "cuvewk"))]
crossing = [wwviw, trtz]
design=[ihaxo,mwabx,drfsq,wwviw,ddx,mehm,trtz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
