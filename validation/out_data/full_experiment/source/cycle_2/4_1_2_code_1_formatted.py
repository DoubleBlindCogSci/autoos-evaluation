### REGULAR FACTORS
chrlaq = Factor("chrlaq", ["tdmy", "jevqi"])
fbxkr = Factor("fbxkr", ["brsx", "soct"])
iuqbla = Factor("iuqbla", ["tdmy", "jevqi"])
mozm = Factor("mozm", ["brsx", "soct"])
### DERIVED FACTORS
##
def stkcrb (mozm, iuqbla):
    return mozm == iuqbla
def qxk (mozm, iuqbla):
    return not stkcrb(mozm, iuqbla)
fjoa = Factor("fjoa", [DerivedLevel("icnyt", WithinTrial(stkcrb, [mozm, iuqbla])), DerivedLevel("ove", WithinTrial(qxk, [mozm, iuqbla]))])
### EXPERIMENT
design=[fjoa,chrlaq,fbxkr,iuqbla,mozm]
constraints=[AtMostKInARow(4, fjoa),ExactlyKInARow(4, fbxkr)]
crossing=[iuqbla,chrlaq]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
