### REGULAR FACTORS
ihaxo = Factor("ihaxo", ["nebj", "gqov"])
mwabx = Factor("mwabx", ["upfna", "qnn"])
drfsq = Factor("drfsq", ["nebj", "gqov"])
wwviw = Factor("wwviw", ["upfna", "qnn"])
ddx = Factor("ddx", ["oesdd", "cgcxdg"])
### DERIVED FACTORS
##
def rkif (wwviw, ddx):
    return wwviw == ddx
def dmlds (wwviw, ddx):
    return not rkif(wwviw, ddx)
mehm = Factor("mehm", [DerivedLevel("onat", WithinTrial(rkif, [wwviw, ddx])), DerivedLevel("zbtzh", WithinTrial(dmlds, [wwviw, ddx]))])
##
def xjcy (drfsq, ihaxo):
    return drfsq == ihaxo
def hlh (drfsq, ihaxo):
    return not xjcy(drfsq, ihaxo)
trtz = Factor("trtz", [DerivedLevel("itvon", WithinTrial(xjcy, [drfsq, ihaxo])), DerivedLevel("cuvewk", WithinTrial(hlh, [drfsq, ihaxo]))])
### EXPERIMENT
design=[mehm,trtz,ihaxo,mwabx,drfsq,wwviw,ddx]
constraints=[ExactlyKInARow(3, trtz),AtLeastKInARow(2, trtz)]
crossing=[wwviw,trtz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
