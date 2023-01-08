### REGULAR FACTORS
updm = Factor("updm", ["etzxb", "jpfb"])
zvkc = Factor("zvkc", ["nrt", "rbvvsb"])
sxwaf = Factor("sxwaf", ["etzxb", "jpfb"])
pcyuwu = Factor("pcyuwu", ["nrt", "rbvvsb"])
### DERIVED FACTORS
##
def is_hbo_oenvuo(zvkc, updm):
    return zvkc == updm
def is_hbo_jnvo(zvkc, updm):
    return not is_hbo_oenvuo(zvkc, updm)
hbo = Factor("hbo", [DerivedLevel("oenvuo", WithinTrial(is_hbo_oenvuo, [zvkc, updm])), DerivedLevel("jnvo", WithinTrial(is_hbo_jnvo, [zvkc, updm]))])
### EXPERIMENT
constraints = []
crossing = [pcyuwu, hbo]
design=[updm,zvkc,sxwaf,pcyuwu,hbo]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
