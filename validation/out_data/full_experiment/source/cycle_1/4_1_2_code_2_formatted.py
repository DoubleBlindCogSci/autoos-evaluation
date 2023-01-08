### REGULAR FACTORS
lno = Factor("lno", ["sudp", "nogr"])
tula = Factor("tula", ["bkcad", "cjm"])
ygadz = Factor("ygadz", ["sudp", "nogr"])
qxlh = Factor("qxlh", ["bkcad", "cjm"])
### DERIVED FACTORS
##
def is_xkx_ezcq(tula, lno):
    return tula == lno
def is_xkx_wgybo(tula, lno):
    return not is_xkx_ezcq(tula, lno)
xkx = Factor("xkx", [DerivedLevel("ezcq", WithinTrial(is_xkx_ezcq, [tula, lno])), DerivedLevel("wgybo", WithinTrial(is_xkx_wgybo, [tula, lno]))])
### EXPERIMENT
constraints = [AtLeastKInARow(3, (tula, "bkcad")), MinimumTrials(28)]
crossing = [qxlh, xkx]
design=[lno,tula,ygadz,qxlh,xkx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
