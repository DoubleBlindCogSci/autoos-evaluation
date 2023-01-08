### REGULAR FACTORS
avbwpg = Factor("avbwpg", ["cimg", "hbfe"])
xzx = Factor("xzx", ["fsk", "nnbtc"])
qrtckt = Factor("qrtckt", ["cimg", "hbfe"])
zomk = Factor("zomk", ["fsk", "nnbtc"])
dergv = Factor("dergv", ["sxzdej", "rxwuo"])
ubzdcu = Factor("ubzdcu", ["vdom", "mqg"])
### DERIVED FACTORS
##
def is_ftmaw_nch(xzx, ubzdcu):
    return xzx == ubzdcu
def is_ftmaw_mfdpop(xzx, ubzdcu):
    return not is_ftmaw_nch(xzx, ubzdcu)
ftmaw = Factor("ftmaw", [DerivedLevel("nch", WithinTrial(is_ftmaw_nch, [xzx, ubzdcu])), DerivedLevel("mfdpop", WithinTrial(is_ftmaw_mfdpop, [xzx, ubzdcu]))])
##
def is_upva_gukug(qrtckt, dergv):
    return qrtckt == dergv
def is_upva_bseu(qrtckt, dergv):
    return not is_upva_gukug(qrtckt, dergv)
upva = Factor("upva", [DerivedLevel("gukug", WithinTrial(is_upva_gukug, [qrtckt, dergv])), DerivedLevel("bseu", WithinTrial(is_upva_bseu, [qrtckt, dergv]))])
### EXPERIMENT
constraints = [MinimumTrials(29)]
crossing = [[dergv, zomk]]
design=[avbwpg,xzx,qrtckt,zomk,dergv,ubzdcu,ftmaw,upva]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
