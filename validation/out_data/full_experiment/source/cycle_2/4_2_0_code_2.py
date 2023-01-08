from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
crs = Factor("crs", ["pmg", "qkb"])
iaqirv = Factor("iaqirv", ["qvcp", "xxpwn"])
ivfjrc = Factor("ivfjrc", ["pmg", "qkb"])
auc = Factor("auc", ["qvcp", "xxpwn"])
def is_iuovx_nqlgn(crs, auc):
    return crs == auc
def is_iuovx_iaajvq(crs, auc):
    return not is_iuovx_nqlgn(crs, auc)
iuovx= Factor("iuovx", [DerivedLevel("nqlgn", WithinTrial(is_iuovx_nqlgn, [crs, auc])), DerivedLevel("iaajvq", WithinTrial(is_iuovx_iaajvq, [crs, auc]))])
def is_mrqv_uegs(iaqirv, ivfjrc):
    return iaqirv == ivfjrc
def is_mrqv_hhguew(iaqirv, ivfjrc):
    return not is_mrqv_uegs(iaqirv, ivfjrc)
mrqv= Factor("mrqv", [DerivedLevel("uegs", WithinTrial(is_mrqv_uegs, [iaqirv, ivfjrc])), DerivedLevel("hhguew", WithinTrial(is_mrqv_hhguew, [iaqirv, ivfjrc]))])
constraints = []
crossing = [mrqv, crs]

design=[crs,iaqirv,ivfjrc,auc,iuovx,mrqv]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_0"))
