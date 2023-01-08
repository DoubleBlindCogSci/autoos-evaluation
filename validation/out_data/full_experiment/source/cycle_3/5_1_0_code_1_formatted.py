### REGULAR FACTORS
dnuay = Factor("dnuay", ["mrja", "aoeg"])
khuiq = Factor("khuiq", ["mvda", "jfwow"])
yqs = Factor("yqs", ["mrja", "aoeg"])
mtarj = Factor("mtarj", ["mvda", "jfwow"])
mhibz = Factor("mhibz", ["eroq", "irtmb"])
### DERIVED FACTORS
##
def xen (mhibz, khuiq):
    return mhibz == khuiq
def lql (mhibz, khuiq):
    return not xen(mhibz, khuiq)
cbgvt = Factor("cbgvt", [DerivedLevel("nxfjfi", WithinTrial(xen, [mhibz, khuiq])), DerivedLevel("dge", WithinTrial(lql, [mhibz, khuiq]))])
### EXPERIMENT
design=[cbgvt,dnuay,khuiq,yqs,mtarj,mhibz]
constraints=[]
crossing=[dnuay,yqs]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
