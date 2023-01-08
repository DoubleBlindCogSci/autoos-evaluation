### REGULAR FACTORS
dodd = Factor("dodd", ["lfk", "qsy"])
vodhe = Factor("vodhe", ["tkttub", "rfctx"])
fnv = Factor("fnv", ["lfk", "qsy"])
fiw = Factor("fiw", ["tkttub", "rfctx"])
### DERIVED FACTORS
##
def is_dvx_ylij(dodd, fiw):
    return dodd == fiw
def is_dvx_gya(dodd, fiw):
    return not is_dvx_ylij(dodd, fiw)
dvx = Factor("dvx", [DerivedLevel("ylij", WithinTrial(is_dvx_ylij, [dodd, fiw])), DerivedLevel("gya", WithinTrial(is_dvx_gya, [dodd, fiw]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, dodd)]
crossing = [fiw, dodd]
design=[dodd,vodhe,fnv,fiw,dvx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
