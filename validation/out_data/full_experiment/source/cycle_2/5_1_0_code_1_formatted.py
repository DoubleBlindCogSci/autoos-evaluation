### REGULAR FACTORS
dtr = Factor("dtr", ["ted", "rqhh"])
wlgsw = Factor("wlgsw", ["pbvh", "zkbz"])
pfj = Factor("pfj", ["ted", "rqhh"])
hbkma = Factor("hbkma", ["pbvh", "zkbz"])
lhe = Factor("lhe", ["dihh", "fpmzkq"])
### DERIVED FACTORS
##
def ywhf (dtr, pfj):
    return dtr == pfj
def irebb (dtr, pfj):
    return not ywhf(dtr, pfj)
sovpx = Factor("sovpx", [DerivedLevel("xfxluk", WithinTrial(ywhf, [dtr, pfj])), DerivedLevel("qmrrzn", WithinTrial(irebb, [dtr, pfj]))])
### EXPERIMENT
design=[sovpx,dtr,wlgsw,pfj,hbkma,lhe]
constraints=[]
crossing=[wlgsw,sovpx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
