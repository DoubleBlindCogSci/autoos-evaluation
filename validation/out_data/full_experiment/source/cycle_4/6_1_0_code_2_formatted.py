### REGULAR FACTORS
nnoqy = Factor("nnoqy", ["xmqn", "tkhwvj"])
bac = Factor("bac", ["isxjfn", "gmpgkr"])
iopjv = Factor("iopjv", ["xmqn", "tkhwvj"])
lnnq = Factor("lnnq", ["isxjfn", "gmpgkr"])
svbto = Factor("svbto", ["wlmdyb", "adjimh"])
mtro = Factor("mtro", ["hgcxa", "frzn"])
### DERIVED FACTORS
##
def is_ggzo_kzir(bac, lnnq):
    return bac == lnnq
def is_ggzo_wddk(bac, lnnq):
    return not is_ggzo_kzir(bac, lnnq)
ggzo = Factor("ggzo", [DerivedLevel("kzir", WithinTrial(is_ggzo_kzir, [bac, lnnq])), DerivedLevel("wddk", WithinTrial(is_ggzo_wddk, [bac, lnnq]))])
### EXPERIMENT
constraints = []
crossing = [iopjv, svbto]
design=[nnoqy,bac,iopjv,lnnq,svbto,mtro,ggzo]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
