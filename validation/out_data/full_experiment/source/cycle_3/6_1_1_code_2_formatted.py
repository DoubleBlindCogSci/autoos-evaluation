### REGULAR FACTORS
opstb = Factor("opstb", ["gizmm", "oaxg"])
hehx = Factor("hehx", ["ewbu", "vai"])
bob = Factor("bob", ["gizmm", "oaxg"])
pdwuqf = Factor("pdwuqf", ["ewbu", "vai"])
pyxfb = Factor("pyxfb", ["cohge", "tdm"])
iwhnba = Factor("iwhnba", ["vehu", "xmcl"])
### DERIVED FACTORS
##
def is_niyyi_ieeoy(bob, pdwuqf):
    return bob == pdwuqf
def is_niyyi_wywxab(bob, pdwuqf):
    return not is_niyyi_ieeoy(bob, pdwuqf)
niyyi = Factor("niyyi", [DerivedLevel("ieeoy", WithinTrial(is_niyyi_ieeoy, [bob, pdwuqf])), DerivedLevel("wywxab", WithinTrial(is_niyyi_wywxab, [bob, pdwuqf]))])
### EXPERIMENT
constraints = [AtLeastKInARow(4, (opstb, "gizmm"))]
crossing = [hehx, pyxfb]
design=[opstb,hehx,bob,pdwuqf,pyxfb,iwhnba,niyyi]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
