### REGULAR FACTORS
crs = Factor("crs", ["pmg", "qkb"])
iaqirv = Factor("iaqirv", ["qvcp", "xxpwn"])
ivfjrc = Factor("ivfjrc", ["pmg", "qkb"])
auc = Factor("auc", ["qvcp", "xxpwn"])
### DERIVED FACTORS
##
def is_iuovx_nqlgn(crs, auc):
    return crs == auc
def is_iuovx_iaajvq(crs, auc):
    return not is_iuovx_nqlgn(crs, auc)
iuovx= Factor("iuovx", [DerivedLevel("nqlgn", WithinTrial(is_iuovx_nqlgn, [crs, auc])), DerivedLevel("iaajvq", WithinTrial(is_iuovx_iaajvq, [crs, auc]))])
##
def is_mrqv_uegs(iaqirv, ivfjrc):
    return iaqirv == ivfjrc
def is_mrqv_hhguew(iaqirv, ivfjrc):
    return not is_mrqv_uegs(iaqirv, ivfjrc)
mrqv= Factor("mrqv", [DerivedLevel("uegs", WithinTrial(is_mrqv_uegs, [iaqirv, ivfjrc])), DerivedLevel("hhguew", WithinTrial(is_mrqv_hhguew, [iaqirv, ivfjrc]))])
### EXPERIMENT
constraints = []
crossing = [mrqv, crs]
design=[crs,iaqirv,ivfjrc,auc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
