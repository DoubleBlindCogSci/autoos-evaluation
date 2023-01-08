### REGULAR FACTORS
jjywqq = Factor("jjywqq", ["ybtpmi", "lqlydm"])
tjwatw = Factor("tjwatw", ["qezqa", "dypoob"])
eayq = Factor("eayq", ["ybtpmi", "lqlydm"])
zlt = Factor("zlt", ["qezqa", "dypoob"])
wgjkb = Factor("wgjkb", ["vajuv", "kapoyj"])
gmrf = Factor("gmrf", ["licx", "qgi"])
### DERIVED FACTORS
##
def aayt (gmrf, zlt):
    return gmrf == zlt
def sgwj (gmrf, zlt):
    return not aayt(gmrf, zlt)
gho = Factor("gho", [DerivedLevel("dnvcxo", WithinTrial(aayt, [gmrf, zlt])), DerivedLevel("fhuy", WithinTrial(sgwj, [gmrf, zlt]))])
##
def ntpmux (wgjkb, tjwatw):
    return wgjkb == tjwatw
def lnlfmi (wgjkb, tjwatw):
    return not ntpmux(wgjkb, tjwatw)
tvz = Factor("tvz", [DerivedLevel("wsalj", WithinTrial(ntpmux, [wgjkb, tjwatw])), DerivedLevel("lopa", WithinTrial(lnlfmi, [wgjkb, tjwatw]))])
### EXPERIMENT
design=[gho,tvz,jjywqq,tjwatw,eayq,zlt,wgjkb,gmrf]
constraints=[ExactlyKInARow(2, tjwatw),MinimumTrials(25)]
crossing=[eayq,gho]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
