### REGULAR FACTORS
qbels = Factor("qbels", ["fedyp", "qvtee"])
zafcwt = Factor("zafcwt", ["jkyqe", "hvpzy"])
gkvi = Factor("gkvi", ["fedyp", "qvtee"])
kfzgby = Factor("kfzgby", ["jkyqe", "hvpzy"])
dpzavt = Factor("dpzavt", ["vnmzjk", "vpgjkg"])
### DERIVED FACTORS
##
def spegxs (kfzgby, gkvi):
    return kfzgby == gkvi
def fspbs (kfzgby, gkvi):
    return not spegxs(kfzgby, gkvi)
hwyre = Factor("hwyre", [DerivedLevel("zdvnk", WithinTrial(spegxs, [kfzgby, gkvi])), DerivedLevel("mxo", WithinTrial(fspbs, [kfzgby, gkvi]))])
##
def hoxtl (zafcwt, dpzavt):
    return zafcwt == dpzavt
def mkv (zafcwt, dpzavt):
    return not hoxtl(zafcwt, dpzavt)
dfznp = Factor("dfznp", [DerivedLevel("gkkww", WithinTrial(hoxtl, [zafcwt, dpzavt])), DerivedLevel("vxtxq", WithinTrial(mkv, [zafcwt, dpzavt]))])
### EXPERIMENT
design=[hwyre,dfznp,qbels,zafcwt,gkvi,kfzgby,dpzavt]
constraints=[ExactlyKInARow(3, qbels),AtLeastKInARow(4, kfzgby)]
crossing=[dfznp,zafcwt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
