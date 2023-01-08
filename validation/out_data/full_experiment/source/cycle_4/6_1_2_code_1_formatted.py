### REGULAR FACTORS
snat = Factor("snat", ["pkijs", "krrj"])
kaqka = Factor("kaqka", ["inqo", "qggwd"])
lvisj = Factor("lvisj", ["pkijs", "krrj"])
gqw = Factor("gqw", ["inqo", "qggwd"])
wkqe = Factor("wkqe", ["cpar", "pcfsm"])
pyoyje = Factor("pyoyje", ["yejf", "aupzma"])
### DERIVED FACTORS
##
def fdr (lvisj, pyoyje):
    return lvisj == pyoyje
def euiuag (lvisj, pyoyje):
    return not fdr(lvisj, pyoyje)
hjip = Factor("hjip", [DerivedLevel("tutcm", WithinTrial(fdr, [lvisj, pyoyje])), DerivedLevel("micqz", WithinTrial(euiuag, [lvisj, pyoyje]))])
##
### EXPERIMENT
design=[hjip,snat,kaqka,lvisj,gqw,wkqe,pyoyje]
constraints=[ExactlyKInARow(4, wkqe),AtMostKInARow(2, snat)]
crossing=[kaqka,hjip]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
