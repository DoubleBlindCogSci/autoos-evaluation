### REGULAR FACTORS
vshu = Factor("vshu", ["delb", "yzyt"])
xekqc = Factor("xekqc", ["zdxu", "ydd"])
xnffn = Factor("xnffn", ["delb", "yzyt"])
dpfsnj = Factor("dpfsnj", ["zdxu", "ydd"])
tpuh = Factor("tpuh", ["dtr", "luunw"])
### DERIVED FACTORS
##
def is_uqdkg_jxmnij(dpfsnj, tpuh):
    return dpfsnj == tpuh
def is_uqdkg_hutd(dpfsnj, tpuh):
    return not is_uqdkg_jxmnij(dpfsnj, tpuh)
uqdkg = Factor("uqdkg", [DerivedLevel("jxmnij", WithinTrial(is_uqdkg_jxmnij, [dpfsnj, tpuh])), DerivedLevel("hutd", WithinTrial(is_uqdkg_hutd, [dpfsnj, tpuh]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, uqdkg)]
crossing = [vshu, tpuh]
design=[vshu,xekqc,xnffn,dpfsnj,tpuh,uqdkg]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
