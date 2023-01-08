### REGULAR FACTORS
dfqk = Factor("dfqk", ["psdz", "flwj"])
ptzx = Factor("ptzx", ["xhsut", "zgap"])
jyg = Factor("jyg", ["psdz", "flwj"])
gqdbe = Factor("gqdbe", ["xhsut", "zgap"])
xgijm = Factor("xgijm", ["swu", "jdvb"])
zlvm = Factor("zlvm", ["fxydov", "qqc"])
### DERIVED FACTORS
##
def is_jczjok_hsh(xgijm, zlvm):
    return xgijm == zlvm
def is_jczjok_eik(xgijm, zlvm):
    return not is_jczjok_hsh(xgijm, zlvm)
jczjok= Factor("jczjok", [DerivedLevel("hsh", WithinTrial(is_jczjok_hsh, [xgijm, zlvm])), DerivedLevel("eik", WithinTrial(is_jczjok_eik, [xgijm, zlvm]))])
### EXPERIMENT
constraints = [MinimumTrials(52), ExactlyK(3, zlvm)]
crossing = [xgijm, dfqk]
design=[dfqk,ptzx,jyg,gqdbe,xgijm,zlvm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
