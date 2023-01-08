### REGULAR FACTORS
chrlaq = Factor("chrlaq", ["tdmy", "jevqi"])
fbxkr = Factor("fbxkr", ["brsx", "soct"])
iuqbla = Factor("iuqbla", ["tdmy", "jevqi"])
mozm = Factor("mozm", ["brsx", "soct"])
### DERIVED FACTORS
##
def is_fjoa_icnyt(mozm, iuqbla):
    return mozm == iuqbla
def is_fjoa_ove(mozm, iuqbla):
    return not is_fjoa_icnyt(mozm, iuqbla)
fjoa= Factor("fjoa", [DerivedLevel("icnyt", WithinTrial(is_fjoa_icnyt, [mozm, iuqbla])), DerivedLevel("ove", WithinTrial(is_fjoa_ove, [mozm, iuqbla]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, fjoa), AtLeastKInARow(4, fbxkr)]
crossing = [iuqbla, chrlaq]
design=[chrlaq,fbxkr,iuqbla,mozm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
