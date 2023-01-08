### REGULAR FACTORS
dcoelt = Factor("dcoelt", ["trehz", "wrla"])
wohi = Factor("wohi", ["kjz", "tnks"])
zhzxp = Factor("zhzxp", ["trehz", "wrla"])
bsp = Factor("bsp", ["kjz", "tnks"])
### DERIVED FACTORS
##
def rhs (dcoelt, wohi):
    return dcoelt == wohi
def zeshbx (dcoelt, wohi):
    return not rhs(dcoelt, wohi)
ryvm = Factor("ryvm", [DerivedLevel("mdvu", WithinTrial(rhs, [dcoelt, wohi])), DerivedLevel("sbgra", WithinTrial(zeshbx, [dcoelt, wohi]))])
##
def cin (zhzxp, bsp):
    return zhzxp == bsp
def drwqm (zhzxp, bsp):
    return not cin(zhzxp, bsp)
uzbpmj = Factor("uzbpmj", [DerivedLevel("ehyn", WithinTrial(cin, [zhzxp, bsp])), DerivedLevel("vslmq", WithinTrial(drwqm, [zhzxp, bsp]))])
### EXPERIMENT
design=[ryvm,uzbpmj,dcoelt,wohi,zhzxp,bsp]
constraints=[MinimumTrials(45)]
crossing=[dcoelt,zhzxp]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
