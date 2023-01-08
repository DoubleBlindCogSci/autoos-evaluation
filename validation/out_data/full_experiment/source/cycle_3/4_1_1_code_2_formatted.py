### REGULAR FACTORS
rzadpo = Factor("rzadpo", ["elxlc", "zim"])
tcx = Factor("tcx", ["oile", "tmxtso"])
mpsi = Factor("mpsi", ["elxlc", "zim"])
qqsuu = Factor("qqsuu", ["oile", "tmxtso"])
### DERIVED FACTORS
##
def is_zyhs_fxyqp(qqsuu, rzadpo):
    return qqsuu == rzadpo
def is_zyhs_nljia(qqsuu, rzadpo):
    return not is_zyhs_fxyqp(qqsuu, rzadpo)
zyhs = Factor("zyhs", [DerivedLevel("fxyqp", WithinTrial(is_zyhs_fxyqp, [qqsuu, rzadpo])), DerivedLevel("nljia", WithinTrial(is_zyhs_nljia, [qqsuu, rzadpo]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, zyhs)]
crossing = [rzadpo, tcx]
design=[rzadpo,tcx,mpsi,qqsuu,zyhs]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
