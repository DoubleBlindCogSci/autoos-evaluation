### REGULAR FACTORS
vshu = Factor("vshu", ["delb", "yzyt"])
xekqc = Factor("xekqc", ["zdxu", "ydd"])
xnffn = Factor("xnffn", ["delb", "yzyt"])
dpfsnj = Factor("dpfsnj", ["zdxu", "ydd"])
tpuh = Factor("tpuh", ["dtr", "luunw"])
### DERIVED FACTORS
##
def vjm (dpfsnj, tpuh):
    return dpfsnj == tpuh
def inony (dpfsnj, tpuh):
    return not vjm(dpfsnj, tpuh)
uqdkg = Factor("uqdkg", [DerivedLevel("jxmnij", WithinTrial(vjm, [dpfsnj, tpuh])), DerivedLevel("hutd", WithinTrial(inony, [dpfsnj, tpuh]))])
##
### EXPERIMENT
design=[uqdkg,vshu,xekqc,xnffn,dpfsnj,tpuh]
constraints=[AtMostKInARow(4, uqdkg)]
crossing=[vshu,tpuh]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
