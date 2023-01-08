### REGULAR FACTORS
kfb = Factor("kfb", ["fvdwcy", "isd"])
awwzy = Factor("awwzy", ["haqh", "nunh"])
moeh = Factor("moeh", ["fvdwcy", "isd"])
hfwn = Factor("hfwn", ["haqh", "nunh"])
### DERIVED FACTORS
##
def is_bvdn_evws(hfwn, awwzy):
    return hfwn == awwzy
def is_bvdn_illqj(hfwn, awwzy):
    return not is_bvdn_evws(hfwn, awwzy)
bvdn = Factor("bvdn", [DerivedLevel("evws", WithinTrial(is_bvdn_evws, [hfwn, awwzy])), DerivedLevel("illqj", WithinTrial(is_bvdn_illqj, [hfwn, awwzy]))])
### EXPERIMENT
constraints = []
crossing = [kfb, awwzy]
design=[kfb,awwzy,moeh,hfwn,bvdn]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
