### REGULAR FACTORS
updm = Factor("updm", ["etzxb", "jpfb"])
zvkc = Factor("zvkc", ["nrt", "rbvvsb"])
sxwaf = Factor("sxwaf", ["etzxb", "jpfb"])
pcyuwu = Factor("pcyuwu", ["nrt", "rbvvsb"])
### DERIVED FACTORS
##
def yazsbf (zvkc, updm):
    return zvkc == updm
def pmxs (zvkc, updm):
    return not yazsbf(zvkc, updm)
hbo = Factor("hbo", [DerivedLevel("oenvuo", WithinTrial(yazsbf, [zvkc, updm])), DerivedLevel("jnvo", WithinTrial(pmxs, [zvkc, updm]))])
### EXPERIMENT
design=[hbo,updm,zvkc,sxwaf,pcyuwu]
constraints=[]
crossing=[pcyuwu,hbo]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
