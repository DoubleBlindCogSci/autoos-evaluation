### REGULAR FACTORS
wbr = Factor("wbr", ["ntmsnw", "fouy"])
wlw = Factor("wlw", ["ycpahd", "eydki"])
pcnmlg = Factor("pcnmlg", ["ntmsnw", "fouy"])
tow = Factor("tow", ["ycpahd", "eydki"])
### DERIVED FACTORS
##
def is_srcywn_icthpl(wlw, tow):
    return wlw == tow
def is_srcywn_txdzmf(wlw, tow):
    return not is_srcywn_icthpl(wlw, tow)
srcywn= Factor("srcywn", [DerivedLevel("icthpl", WithinTrial(is_srcywn_icthpl, [wlw, tow])), DerivedLevel("txdzmf", WithinTrial(is_srcywn_txdzmf, [wlw, tow]))])
### EXPERIMENT
constraints = []
crossing = [wbr, wlw]
design=[wbr,wlw,pcnmlg,tow]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
