### REGULAR FACTORS
ozffyg = Factor("ozffyg", ["ktpg", "ezgdye"])
eor = Factor("eor", ["bvwt", "odzvfn"])
ulmvu = Factor("ulmvu", ["ktpg", "ezgdye"])
ydyizj = Factor("ydyizj", ["bvwt", "odzvfn"])
### DERIVED FACTORS
##
def vyt(eor, ydyizj):
    return eor == ydyizj
def zfu(eor, ydyizj):
    return not vyt(eor, ydyizj)
vnud = Factor("vnud", [DerivedLevel("cmru", WithinTrial(vyt, [eor, ydyizj])), DerivedLevel("hjfu", WithinTrial(zfu, [eor, ydyizj]))])
### EXPERIMENT
constraints = [AtMostKInARow(3, vnud)]
crossing = [ulmvu, vnud]
design=[ozffyg,eor,ulmvu,ydyizj,vnud]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
