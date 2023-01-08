### REGULAR FACTORS
wbr = Factor("wbr", ["ntmsnw", "fouy"])
wlw = Factor("wlw", ["ycpahd", "eydki"])
pcnmlg = Factor("pcnmlg", ["ntmsnw", "fouy"])
tow = Factor("tow", ["ycpahd", "eydki"])
### DERIVED FACTORS
##
def ijfamm (wlw, tow):
    return wlw == tow
def oxrtfi (wlw, tow):
    return not ijfamm(wlw, tow)
srcywn = Factor("srcywn", [DerivedLevel("icthpl", WithinTrial(ijfamm, [wlw, tow])), DerivedLevel("txdzmf", WithinTrial(oxrtfi, [wlw, tow]))])
##
### EXPERIMENT
design=[srcywn,wbr,wlw,pcnmlg,tow]
constraints=[]
crossing=[wbr,wlw]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
