### REGULAR FACTORS
oxt = Factor("oxt", ["sivho", "cqbgic"])
jvg = Factor("jvg", ["ohs", "wpyrc"])
moskvk = Factor("moskvk", ["sivho", "cqbgic"])
ijmr = Factor("ijmr", ["ohs", "wpyrc"])
### DERIVED FACTORS
##
def mlbfmb (ijmr, moskvk):
    return ijmr == moskvk
def zuegl (ijmr, moskvk):
    return not mlbfmb(ijmr, moskvk)
knmejn = Factor("knmejn", [DerivedLevel("dhmqoa", WithinTrial(mlbfmb, [ijmr, moskvk])), DerivedLevel("tgtul", WithinTrial(zuegl, [ijmr, moskvk]))])
##
def njsh (oxt, jvg):
    return oxt == jvg
def apbpic (oxt, jvg):
    return not njsh(oxt, jvg)
imxuu = Factor("imxuu", [DerivedLevel("ajirpt", WithinTrial(njsh, [oxt, jvg])), DerivedLevel("nozlj", WithinTrial(apbpic, [oxt, jvg]))])
### EXPERIMENT
design=[knmejn,imxuu,oxt,jvg,moskvk,ijmr]
constraints=[AtMostKInARow(2, oxt)]
crossing=[moskvk,oxt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
