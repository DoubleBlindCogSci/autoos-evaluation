### REGULAR FACTORS
vkjko = Factor("vkjko", ["fga", "pdoq"])
wgrgtc = Factor("wgrgtc", ["bbwayz", "tmthev"])
wewe = Factor("wewe", ["fga", "pdoq"])
jkhd = Factor("jkhd", ["bbwayz", "tmthev"])
oir = Factor("oir", ["bjpq", "sfjahf"])
### DERIVED FACTORS
##
def mqob (oir, jkhd):
    return oir == jkhd
def ubgfkw (oir, jkhd):
    return not mqob(oir, jkhd)
eivlb = Factor("eivlb", [DerivedLevel("irho", WithinTrial(mqob, [oir, jkhd])), DerivedLevel("hjbpis", WithinTrial(ubgfkw, [oir, jkhd]))])
### EXPERIMENT
design=[eivlb,vkjko,wgrgtc,wewe,jkhd,oir]
constraints=[MinimumTrials(26)]
crossing=[wgrgtc,eivlb]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
