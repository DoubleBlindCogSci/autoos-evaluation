### REGULAR FACTORS
dfqk = Factor("dfqk", ["psdz", "flwj"])
ptzx = Factor("ptzx", ["xhsut", "zgap"])
jyg = Factor("jyg", ["psdz", "flwj"])
gqdbe = Factor("gqdbe", ["xhsut", "zgap"])
xgijm = Factor("xgijm", ["swu", "jdvb"])
zlvm = Factor("zlvm", ["fxydov", "qqc"])
### DERIVED FACTORS
##
def wlyd (xgijm, zlvm):
    return xgijm == zlvm
def qsnv (xgijm, zlvm):
    return not wlyd(xgijm, zlvm)
jczjok = Factor("jczjok", [DerivedLevel("hsh", WithinTrial(wlyd, [xgijm, zlvm])), DerivedLevel("eik", WithinTrial(qsnv, [xgijm, zlvm]))])
##
### EXPERIMENT
design=[jczjok,dfqk,ptzx,jyg,gqdbe,xgijm,zlvm]
constraints=[ExactlyKInARow(3, zlvm),MinimumTrials(52)]
crossing=[xgijm,dfqk]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
