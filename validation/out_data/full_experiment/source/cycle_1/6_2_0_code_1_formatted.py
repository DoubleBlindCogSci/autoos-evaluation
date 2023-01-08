### REGULAR FACTORS
vce = Factor("vce", ["lblh", "uer"])
nacsbx = Factor("nacsbx", ["dykns", "fhnvoo"])
nqydwt = Factor("nqydwt", ["lblh", "uer"])
nizx = Factor("nizx", ["dykns", "fhnvoo"])
qlbbhb = Factor("qlbbhb", ["grviw", "njrmn"])
mmbm = Factor("mmbm", ["fqzevn", "qstpt"])
### DERIVED FACTORS
##
def qfvl (nizx, mmbm):
    return nizx == mmbm
def iposdx (nizx, mmbm):
    return not qfvl(nizx, mmbm)
yayb = Factor("yayb", [DerivedLevel("uvqryf", WithinTrial(qfvl, [nizx, mmbm])), DerivedLevel("uaty", WithinTrial(iposdx, [nizx, mmbm]))])
##
def rgc (nqydwt, vce):
    return nqydwt == vce
def jxua (nqydwt, vce):
    return not rgc(nqydwt, vce)
wwukd = Factor("wwukd", [DerivedLevel("qrmzj", WithinTrial(rgc, [nqydwt, vce])), DerivedLevel("cvihx", WithinTrial(jxua, [nqydwt, vce]))])
### EXPERIMENT
design=[yayb,wwukd,vce,nacsbx,nqydwt,nizx,qlbbhb,mmbm]
constraints=[]
crossing=[nqydwt,nacsbx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
