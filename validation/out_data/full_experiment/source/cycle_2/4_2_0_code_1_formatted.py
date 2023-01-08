### REGULAR FACTORS
crs = Factor("crs", ["pmg", "qkb"])
iaqirv = Factor("iaqirv", ["qvcp", "xxpwn"])
ivfjrc = Factor("ivfjrc", ["pmg", "qkb"])
auc = Factor("auc", ["qvcp", "xxpwn"])
### DERIVED FACTORS
##
def nkx (crs, auc):
    return crs == auc
def pwrq (crs, auc):
    return not nkx(crs, auc)
iuovx = Factor("iuovx", [DerivedLevel("nqlgn", WithinTrial(nkx, [crs, auc])), DerivedLevel("iaajvq", WithinTrial(pwrq, [crs, auc]))])
##
def pqq (iaqirv, ivfjrc):
    return iaqirv == ivfjrc
def qyit (iaqirv, ivfjrc):
    return not pqq(iaqirv, ivfjrc)
mrqv = Factor("mrqv", [DerivedLevel("uegs", WithinTrial(pqq, [iaqirv, ivfjrc])), DerivedLevel("hhguew", WithinTrial(qyit, [iaqirv, ivfjrc]))])
### EXPERIMENT
design=[iuovx,mrqv,crs,iaqirv,ivfjrc,auc]
constraints=[]
crossing=[mrqv,crs]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
