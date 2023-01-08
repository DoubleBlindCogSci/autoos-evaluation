### REGULAR FACTORS
snat = Factor("snat", ["pkijs", "krrj"])
kaqka = Factor("kaqka", ["inqo", "qggwd"])
lvisj = Factor("lvisj", ["pkijs", "krrj"])
gqw = Factor("gqw", ["inqo", "qggwd"])
wkqe = Factor("wkqe", ["cpar", "pcfsm"])
pyoyje = Factor("pyoyje", ["yejf", "aupzma"])
### DERIVED FACTORS
##
def is_hjip_tutcm(lvisj, pyoyje):
    return lvisj == pyoyje
def is_hjip_micqz(lvisj, pyoyje):
    return not is_hjip_tutcm(lvisj, pyoyje)
hjip = Factor("hjip", [DerivedLevel("tutcm", WithinTrial(is_hjip_tutcm, [lvisj, pyoyje])), DerivedLevel("micqz", WithinTrial(is_hjip_micqz, [lvisj, pyoyje]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, snat), AtLeastKInARow(4, wkqe)]
crossing = [kaqka, hjip]
design=[snat,kaqka,lvisj,gqw,wkqe,pyoyje,hjip]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
