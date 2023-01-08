### REGULAR FACTORS
dodd = Factor("dodd", ["lfk", "qsy"])
vodhe = Factor("vodhe", ["tkttub", "rfctx"])
fnv = Factor("fnv", ["lfk", "qsy"])
fiw = Factor("fiw", ["tkttub", "rfctx"])
### DERIVED FACTORS
##
def kcv (dodd, fiw):
    return dodd == fiw
def ork (dodd, fiw):
    return not kcv(dodd, fiw)
dvx = Factor("dvx", [DerivedLevel("ylij", WithinTrial(kcv, [dodd, fiw])), DerivedLevel("gya", WithinTrial(ork, [dodd, fiw]))])
##
### EXPERIMENT
design=[dvx,dodd,vodhe,fnv,fiw]
constraints=[AtMostKInARow(4, dodd)]
crossing=[fiw,dodd]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
