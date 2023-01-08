### REGULAR FACTORS
mojan = Factor("mojan", ["nwu", "psksh"])
odmmgw = Factor("odmmgw", ["gji", "vois"])
xbk = Factor("xbk", ["nwu", "psksh"])
kvkn = Factor("kvkn", ["gji", "vois"])
pypwky = Factor("pypwky", ["rmnym", "pthd"])
### DERIVED FACTORS
##
def flzpm (mojan, odmmgw):
    return mojan == odmmgw
def iopgqj (mojan, odmmgw):
    return not flzpm(mojan, odmmgw)
qsms = Factor("qsms", [DerivedLevel("czo", WithinTrial(flzpm, [mojan, odmmgw])), DerivedLevel("ohxl", WithinTrial(iopgqj, [mojan, odmmgw]))])
##
def kxfddw (xbk, pypwky):
    return xbk == pypwky
def dxjlog (xbk, pypwky):
    return not kxfddw(xbk, pypwky)
jlt = Factor("jlt", [DerivedLevel("szftzq", WithinTrial(kxfddw, [xbk, pypwky])), DerivedLevel("ncfc", WithinTrial(dxjlog, [xbk, pypwky]))])
### EXPERIMENT
design=[qsms,jlt,mojan,odmmgw,xbk,kvkn,pypwky]
constraints=[AtMostKInARow(4, qsms)]
crossing=[jlt,qsms]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
