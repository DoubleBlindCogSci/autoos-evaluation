### REGULAR FACTORS
yvt = Factor("yvt", ["aspg", "mypy"])
nwy = Factor("nwy", ["ludty", "sniosf"])
shy = Factor("shy", ["aspg", "mypy"])
yvnfyr = Factor("yvnfyr", ["ludty", "sniosf"])
eqhnnb = Factor("eqhnnb", ["xjf", "oxjjzy"])
### DERIVED FACTORS
##
def jwc (eqhnnb, yvt):
    return eqhnnb == yvt
def msqcoq (eqhnnb, yvt):
    return not jwc(eqhnnb, yvt)
cdf = Factor("cdf", [DerivedLevel("rprpk", WithinTrial(jwc, [eqhnnb, yvt])), DerivedLevel("zydsnt", WithinTrial(msqcoq, [eqhnnb, yvt]))])
##
### EXPERIMENT
design=[cdf,yvt,nwy,shy,yvnfyr,eqhnnb]
constraints=[AtMostKInARow(4, yvt),MinimumTrials(32)]
crossing=[yvt,yvnfyr]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
