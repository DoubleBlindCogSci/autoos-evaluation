### REGULAR FACTORS
vce = Factor("vce", ["lblh", "uer"])
nacsbx = Factor("nacsbx", ["dykns", "fhnvoo"])
nqydwt = Factor("nqydwt", ["lblh", "uer"])
nizx = Factor("nizx", ["dykns", "fhnvoo"])
qlbbhb = Factor("qlbbhb", ["grviw", "njrmn"])
mmbm = Factor("mmbm", ["fqzevn", "qstpt"])
### DERIVED FACTORS
##
def is_yayb_uvqryf(nizx, mmbm):
    return nizx == mmbm
def is_yayb_uaty(nizx, mmbm):
    return not is_yayb_uvqryf(nizx, mmbm)
yayb= Factor("yayb", [DerivedLevel("uvqryf", WithinTrial(is_yayb_uvqryf, [nizx, mmbm])), DerivedLevel("uaty", WithinTrial(is_yayb_uaty, [nizx, mmbm]))])
##
def is_wwukd_qrmzj(nqydwt, vce):
    return nqydwt == vce
def is_wwukd_cvihx(nqydwt, vce):
    return not is_wwukd_qrmzj(nqydwt, vce)
wwukd= Factor("wwukd", [DerivedLevel("qrmzj", WithinTrial(is_wwukd_qrmzj, [nqydwt, vce])), DerivedLevel("cvihx", WithinTrial(is_wwukd_cvihx, [nqydwt, vce]))])
### EXPERIMENT
constraints = []
crossing = [nqydwt, nacsbx]
design=[vce,nacsbx,nqydwt,nizx,qlbbhb,mmbm]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
