### REGULAR FACTORS
cxac = Factor("cxac", ["alpai", "mdiei"])
byvob = Factor("byvob", ["juc", "bzdi"])
ayfgq = Factor("ayfgq", ["alpai", "mdiei"])
tnd = Factor("tnd", ["juc", "bzdi"])
uwgbrp = Factor("uwgbrp", ["gnyajh", "bqg"])
phb = Factor("phb", ["mjyfwo", "jea"])
### DERIVED FACTORS
##
def mls (phb, uwgbrp):
    return phb == uwgbrp
def dcczs (phb, uwgbrp):
    return not mls(phb, uwgbrp)
funv = Factor("funv", [DerivedLevel("jrhlqv", WithinTrial(mls, [phb, uwgbrp])), DerivedLevel("axyuo", WithinTrial(dcczs, [phb, uwgbrp]))])
##
def poa (cxac, tnd):
    return cxac == tnd
def kmfob (cxac, tnd):
    return not poa(cxac, tnd)
bkcnhy = Factor("bkcnhy", [DerivedLevel("cfae", WithinTrial(poa, [cxac, tnd])), DerivedLevel("ljbbi", WithinTrial(kmfob, [cxac, tnd]))])
### EXPERIMENT
design=[funv,bkcnhy,cxac,byvob,ayfgq,tnd,uwgbrp,phb]
constraints=[AtLeastKInARow(3, byvob),AtMostKInARow(4, uwgbrp)]
crossing=[cxac,byvob]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
