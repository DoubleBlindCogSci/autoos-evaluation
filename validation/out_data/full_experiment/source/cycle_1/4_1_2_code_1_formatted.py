### REGULAR FACTORS
lno = Factor("lno", ["sudp", "nogr"])
tula = Factor("tula", ["bkcad", "cjm"])
ygadz = Factor("ygadz", ["sudp", "nogr"])
qxlh = Factor("qxlh", ["bkcad", "cjm"])
### DERIVED FACTORS
##
def dcbt (tula, lno):
    return tula == lno
def ygvz (tula, lno):
    return not dcbt(tula, lno)
xkx = Factor("xkx", [DerivedLevel("ezcq", WithinTrial(dcbt, [tula, lno])), DerivedLevel("wgybo", WithinTrial(ygvz, [tula, lno]))])
### EXPERIMENT
design=[xkx,lno,tula,ygadz,qxlh]
constraints=[MinimumTrials(28),AtLeastKInARow(3, tula)]
crossing=[qxlh,xkx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
