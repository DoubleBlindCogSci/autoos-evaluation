### REGULAR FACTORS
dnuay = Factor("dnuay", ["mrja", "aoeg"])
khuiq = Factor("khuiq", ["mvda", "jfwow"])
yqs = Factor("yqs", ["mrja", "aoeg"])
mtarj = Factor("mtarj", ["mvda", "jfwow"])
mhibz = Factor("mhibz", ["eroq", "irtmb"])
### DERIVED FACTORS
##
def is_cbgvt_nxfjfi(mhibz, khuiq):
    return mhibz == khuiq
def is_cbgvt_dge(mhibz, khuiq):
    return not is_cbgvt_nxfjfi(mhibz, khuiq)
cbgvt = Factor("cbgvt", [DerivedLevel("nxfjfi", WithinTrial(is_cbgvt_nxfjfi, [mhibz, khuiq])), DerivedLevel("dge", WithinTrial(is_cbgvt_dge, [mhibz, khuiq]))])
### EXPERIMENT
constraints = []
crossing = [dnuay, yqs]
design=[dnuay,khuiq,yqs,mtarj,mhibz,cbgvt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
