### REGULAR FACTORS
vkjko = Factor("vkjko", ["fga", "pdoq"])
wgrgtc = Factor("wgrgtc", ["bbwayz", "tmthev"])
wewe = Factor("wewe", ["fga", "pdoq"])
jkhd = Factor("jkhd", ["bbwayz", "tmthev"])
oir = Factor("oir", ["bjpq", "sfjahf"])
### DERIVED FACTORS
##
def is_eivlb_irho(oir, jkhd):
    return oir == jkhd
def is_eivlb_hjbpis(oir, jkhd):
    return not is_eivlb_irho(oir, jkhd)
eivlb = Factor("eivlb", [DerivedLevel("irho", WithinTrial(is_eivlb_irho, [oir, jkhd])), DerivedLevel("hjbpis", WithinTrial(is_eivlb_hjbpis, [oir, jkhd]))])
### EXPERIMENT
constraints = [MinimumTrials(26)]
crossing = [[wgrgtc, eivlb]]
design=[vkjko,wgrgtc,wewe,jkhd,oir,eivlb]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
