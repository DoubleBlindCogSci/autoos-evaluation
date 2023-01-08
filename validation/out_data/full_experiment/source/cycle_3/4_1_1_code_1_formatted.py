### REGULAR FACTORS
rzadpo = Factor("rzadpo", ["elxlc", "zim"])
tcx = Factor("tcx", ["oile", "tmxtso"])
mpsi = Factor("mpsi", ["elxlc", "zim"])
qqsuu = Factor("qqsuu", ["oile", "tmxtso"])
### DERIVED FACTORS
##
def mfrcwh (qqsuu, rzadpo):
    return qqsuu == rzadpo
def rqhax (qqsuu, rzadpo):
    return not mfrcwh(qqsuu, rzadpo)
zyhs = Factor("zyhs", [DerivedLevel("fxyqp", WithinTrial(mfrcwh, [qqsuu, rzadpo])), DerivedLevel("nljia", WithinTrial(rqhax, [qqsuu, rzadpo]))])
### EXPERIMENT
design=[zyhs,rzadpo,tcx,mpsi,qqsuu]
constraints=[AtMostKInARow(4, zyhs)]
crossing=[rzadpo,tcx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
