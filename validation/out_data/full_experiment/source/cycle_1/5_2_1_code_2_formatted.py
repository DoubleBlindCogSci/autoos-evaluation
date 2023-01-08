### REGULAR FACTORS
mojan = Factor("mojan", ["nwu", "psksh"])
odmmgw = Factor("odmmgw", ["gji", "vois"])
xbk = Factor("xbk", ["nwu", "psksh"])
kvkn = Factor("kvkn", ["gji", "vois"])
pypwky = Factor("pypwky", ["rmnym", "pthd"])
### DERIVED FACTORS
##
def is_qsms_czo(mojan, odmmgw):
    return mojan == odmmgw
def is_qsms_ohxl(mojan, odmmgw):
    return not is_qsms_czo(mojan, odmmgw)
qsms= Factor("qsms", [DerivedLevel("czo", WithinTrial(is_qsms_czo, [mojan, odmmgw])), DerivedLevel("ohxl", WithinTrial(is_qsms_ohxl, [mojan, odmmgw]))])
##
def is_jlt_szftzq(xbk, pypwky):
    return xbk == pypwky
def is_jlt_ncfc(xbk, pypwky):
    return not is_jlt_szftzq(xbk, pypwky)
jlt= Factor("jlt", [DerivedLevel("szftzq", WithinTrial(is_jlt_szftzq, [xbk, pypwky])), DerivedLevel("ncfc", WithinTrial(is_jlt_ncfc, [xbk, pypwky]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, qsms)]
crossing = [jlt, qsms]
design=[mojan,odmmgw,xbk,kvkn,pypwky,qsms,jlt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
