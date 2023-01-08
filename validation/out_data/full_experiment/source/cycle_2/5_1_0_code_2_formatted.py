### REGULAR FACTORS
dtr = Factor("dtr", ["ted", "rqhh"])
wlgsw = Factor("wlgsw", ["pbvh", "zkbz"])
pfj = Factor("pfj", ["ted", "rqhh"])
hbkma = Factor("hbkma", ["pbvh", "zkbz"])
lhe = Factor("lhe", ["dihh", "fpmzkq"])
### DERIVED FACTORS
##
def is_sovpx_xfxluk(dtr, pfj):
    return dtr == pfj
def is_sovpx_qmrrzn(dtr, pfj):
    return not is_sovpx_xfxluk(dtr, pfj)
sovpx= Factor("sovpx", [DerivedLevel("xfxluk", WithinTrial(is_sovpx_xfxluk, [dtr, pfj])), DerivedLevel("qmrrzn", WithinTrial(is_sovpx_qmrrzn, [dtr, pfj]))])
### EXPERIMENT
constraints = []
crossing = [wlgsw, sovpx]
design=[dtr,wlgsw,pfj,hbkma,lhe]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
