### REGULAR FACTORS
kxk = Factor("kxk", ["nllpb", "nhg"])
oqba = Factor("oqba", ["bdalt", "xjsf"])
voo = Factor("voo", ["nllpb", "nhg"])
wtq = Factor("wtq", ["bdalt", "xjsf"])
isf = Factor("isf", ["lavu", "tqntet"])
### DERIVED FACTORS
##
def jeghv(voo, oqba):
    return voo == oqba
def tadi(voo, oqba):
    return not jeghv(voo, oqba)
vceeea = Factor("vceeea", [DerivedLevel("rpds", WithinTrial(jeghv, [voo, oqba])), DerivedLevel("rth", WithinTrial(tadi, [voo, oqba]))])
### EXPERIMENT
constraints = []
crossing = [kxk, voo]
design=[kxk,oqba,voo,wtq,isf,vceeea]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
