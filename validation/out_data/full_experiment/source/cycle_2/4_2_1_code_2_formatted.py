### REGULAR FACTORS
oxt = Factor("oxt", ["sivho", "cqbgic"])
jvg = Factor("jvg", ["ohs", "wpyrc"])
moskvk = Factor("moskvk", ["sivho", "cqbgic"])
ijmr = Factor("ijmr", ["ohs", "wpyrc"])
### DERIVED FACTORS
##
def is_knmejn_dhmqoa(ijmr, moskvk):
    return ijmr == moskvk
def is_knmejn_tgtul(ijmr, moskvk):
    return not is_knmejn_dhmqoa(ijmr, moskvk)
knmejn= Factor("knmejn", [DerivedLevel("dhmqoa", WithinTrial(is_knmejn_dhmqoa, [ijmr, moskvk])), DerivedLevel("tgtul", WithinTrial(is_knmejn_tgtul, [ijmr, moskvk]))])
##
def is_imxuu_ajirpt(oxt, jvg):
    return oxt == jvg
def is_imxuu_nozlj(oxt, jvg):
    return not is_imxuu_ajirpt(oxt, jvg)
imxuu= Factor("imxuu", [DerivedLevel("ajirpt", WithinTrial(is_imxuu_ajirpt, [oxt, jvg])), DerivedLevel("nozlj", WithinTrial(is_imxuu_nozlj, [oxt, jvg]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, oxt)]
crossing = [moskvk, oxt]
design=[oxt,jvg,moskvk,ijmr]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
