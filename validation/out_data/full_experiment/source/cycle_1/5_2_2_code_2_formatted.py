### REGULAR FACTORS
qbels = Factor("qbels", ["fedyp", "qvtee"])
zafcwt = Factor("zafcwt", ["jkyqe", "hvpzy"])
gkvi = Factor("gkvi", ["fedyp", "qvtee"])
kfzgby = Factor("kfzgby", ["jkyqe", "hvpzy"])
dpzavt = Factor("dpzavt", ["vnmzjk", "vpgjkg"])
### DERIVED FACTORS
##
def is_hwyre_zdvnk(kfzgby, gkvi):
    return kfzgby == gkvi
def is_hwyre_mxo(kfzgby, gkvi):
    return not is_hwyre_zdvnk(kfzgby, gkvi)
hwyre= Factor("hwyre", [DerivedLevel("zdvnk", WithinTrial(is_hwyre_zdvnk, [kfzgby, gkvi])), DerivedLevel("mxo", WithinTrial(is_hwyre_mxo, [kfzgby, gkvi]))])
##
def is_dfznp_gkkww(zafcwt, dpzavt):
    return zafcwt == dpzavt
def is_dfznp_vxtxq(zafcwt, dpzavt):
    return not is_dfznp_gkkww(zafcwt, dpzavt)
dfznp= Factor("dfznp", [DerivedLevel("gkkww", WithinTrial(is_dfznp_gkkww, [zafcwt, dpzavt])), DerivedLevel("vxtxq", WithinTrial(is_dfznp_vxtxq, [zafcwt, dpzavt]))])
### EXPERIMENT
constraints = [ExactlyKInARow(3, (qbels, "fedyp")), AtLeastKInARow(4, (kfzgby, "jkyqe"))]
crossing = [dfznp, zafcwt]
design=[qbels,zafcwt,gkvi,kfzgby,dpzavt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
