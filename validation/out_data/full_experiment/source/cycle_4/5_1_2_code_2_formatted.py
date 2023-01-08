### REGULAR FACTORS
yvt = Factor("yvt", ["aspg", "mypy"])
nwy = Factor("nwy", ["ludty", "sniosf"])
shy = Factor("shy", ["aspg", "mypy"])
yvnfyr = Factor("yvnfyr", ["ludty", "sniosf"])
eqhnnb = Factor("eqhnnb", ["xjf", "oxjjzy"])
### DERIVED FACTORS
##
def is_cdf_rprpk(eqhnnb, yvt):
    return eqhnnb == yvt
def is_cdf_zydsnt(eqhnnb, yvt):
    return not is_cdf_rprpk(eqhnnb, yvt)
cdf = Factor("cdf", [DerivedLevel("rprpk", WithinTrial(is_cdf_rprpk, [eqhnnb, yvt])), DerivedLevel("zydsnt", WithinTrial(is_cdf_zydsnt, [eqhnnb, yvt]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, yvt), MinimumTrials(32)]
crossing = [yvt, yvnfyr]
design=[yvt,nwy,shy,yvnfyr,eqhnnb,cdf]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
