### REGULAR FACTORS
rwbf = Factor("rwbf", ["wnxvop", "xpjtji"])
pfval = Factor("pfval", ["vxwj", "nwvr"])
tmqk = Factor("tmqk", ["wnxvop", "xpjtji"])
zay = Factor("zay", ["vxwj", "nwvr"])
axn = Factor("axn", ["ifj", "wrhjrn"])
dwra = Factor("dwra", ["nbowyy", "jxen"])
### DERIVED FACTORS
##
def is_wwbdfd_stfge(rwbf, tmqk):
    return rwbf == tmqk
def is_wwbdfd_gfxw(rwbf, tmqk):
    return not is_wwbdfd_stfge(rwbf, tmqk)
wwbdfd= Factor("wwbdfd", [DerivedLevel("stfge", WithinTrial(is_wwbdfd_stfge, [rwbf, tmqk])), DerivedLevel("gfxw", WithinTrial(is_wwbdfd_gfxw, [rwbf, tmqk]))])
##
def is_zyaxqg_oxlyic(pfval, dwra):
    return pfval == dwra
def is_zyaxqg_cmfig(pfval, dwra):
    return not is_zyaxqg_oxlyic(pfval, dwra)
zyaxqg= Factor("zyaxqg", [DerivedLevel("oxlyic", WithinTrial(is_zyaxqg_oxlyic, [pfval, dwra])), DerivedLevel("cmfig", WithinTrial(is_zyaxqg_cmfig, [pfval, dwra]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, wwbdfd)]
crossing = [dwra, zyaxqg]
design=[rwbf,pfval,tmqk,zay,axn,dwra]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
