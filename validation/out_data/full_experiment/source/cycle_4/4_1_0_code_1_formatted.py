### REGULAR FACTORS
kfb = Factor("kfb", ["fvdwcy", "isd"])
awwzy = Factor("awwzy", ["haqh", "nunh"])
moeh = Factor("moeh", ["fvdwcy", "isd"])
hfwn = Factor("hfwn", ["haqh", "nunh"])
### DERIVED FACTORS
##
def fwmm (hfwn, awwzy):
    return hfwn == awwzy
def lcnpn (hfwn, awwzy):
    return not fwmm(hfwn, awwzy)
bvdn = Factor("bvdn", [DerivedLevel("evws", WithinTrial(fwmm, [hfwn, awwzy])), DerivedLevel("illqj", WithinTrial(lcnpn, [hfwn, awwzy]))])
### EXPERIMENT
design=[bvdn,kfb,awwzy,moeh,hfwn]
constraints=[]
crossing=[kfb,awwzy]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
