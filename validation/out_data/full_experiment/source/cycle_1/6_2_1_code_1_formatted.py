### REGULAR FACTORS
wwr = Factor("wwr", ["tbuiey", "yytduo"])
dnj = Factor("dnj", ["qarhs", "dxt"])
oskly = Factor("oskly", ["tbuiey", "yytduo"])
kny = Factor("kny", ["qarhs", "dxt"])
wgpxd = Factor("wgpxd", ["irlh", "cawso"])
bamy = Factor("bamy", ["qdmmba", "ueqq"])
### DERIVED FACTORS
##
def hycy (kny, bamy):
    return kny == bamy
def uwp (kny, bamy):
    return not hycy(kny, bamy)
rqrk = Factor("rqrk", [DerivedLevel("gqu", WithinTrial(hycy, [kny, bamy])), DerivedLevel("rrpfp", WithinTrial(uwp, [kny, bamy]))])
##
def oluf (wwr, oskly):
    return wwr == oskly
def yjofe (wwr, oskly):
    return not oluf(wwr, oskly)
sppmi = Factor("sppmi", [DerivedLevel("wzd", WithinTrial(oluf, [wwr, oskly])), DerivedLevel("pnrapu", WithinTrial(yjofe, [wwr, oskly]))])
### EXPERIMENT
design=[rqrk,sppmi,wwr,dnj,oskly,kny,wgpxd,bamy]
constraints=[AtMostKInARow(2, dnj)]
crossing=[oskly,wwr]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
