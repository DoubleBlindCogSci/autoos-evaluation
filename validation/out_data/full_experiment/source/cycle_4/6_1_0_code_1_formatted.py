### REGULAR FACTORS
nnoqy = Factor("nnoqy", ["xmqn", "tkhwvj"])
bac = Factor("bac", ["isxjfn", "gmpgkr"])
iopjv = Factor("iopjv", ["xmqn", "tkhwvj"])
lnnq = Factor("lnnq", ["isxjfn", "gmpgkr"])
svbto = Factor("svbto", ["wlmdyb", "adjimh"])
mtro = Factor("mtro", ["hgcxa", "frzn"])
### DERIVED FACTORS
##
def nhlkq (bac, lnnq):
    return bac == lnnq
def wiqa (bac, lnnq):
    return not nhlkq(bac, lnnq)
ggzo = Factor("ggzo", [DerivedLevel("kzir", WithinTrial(nhlkq, [bac, lnnq])), DerivedLevel("wddk", WithinTrial(wiqa, [bac, lnnq]))])
##
### EXPERIMENT
design=[ggzo,nnoqy,bac,iopjv,lnnq,svbto,mtro]
constraints=[]
crossing=[iopjv,svbto]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
