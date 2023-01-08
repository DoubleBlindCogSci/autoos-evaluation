### REGULAR FACTORS
wwr = Factor("wwr", ["tbuiey", "yytduo"])
dnj = Factor("dnj", ["qarhs", "dxt"])
oskly = Factor("oskly", ["tbuiey", "yytduo"])
kny = Factor("kny", ["qarhs", "dxt"])
wgpxd = Factor("wgpxd", ["irlh", "cawso"])
bamy = Factor("bamy", ["qdmmba", "ueqq"])
### DERIVED FACTORS
##
def is_rqrk_gqu(kny, bamy):
    return kny == bamy
def is_rqrk_rrpfp(kny, bamy):
    return not is_rqrk_gqu(kny, bamy)
rqrk= Factor("rqrk", [DerivedLevel("gqu", WithinTrial(is_rqrk_gqu, [kny, bamy])), DerivedLevel("rrpfp", WithinTrial(is_rqrk_rrpfp, [kny, bamy]))])
##
def is_sppmi_wzd(wwr, oskly):
    return wwr == oskly
def is_sppmi_pnrapu(wwr, oskly):
    return not is_sppmi_wzd(wwr, oskly)
sppmi= Factor("sppmi", [DerivedLevel("wzd", WithinTrial(is_sppmi_wzd, [wwr, oskly])), DerivedLevel("pnrapu", WithinTrial(is_sppmi_pnrapu, [wwr, oskly]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, dnj)]
crossing = [oskly, wwr]
design=[wwr,dnj,oskly,kny,wgpxd,bamy]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
