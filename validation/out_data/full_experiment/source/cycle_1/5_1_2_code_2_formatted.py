### REGULAR FACTORS
loslz = Factor("loslz", ["acnxo", "igqh"])
odd = Factor("odd", ["bojkc", "phe"])
mefc = Factor("mefc", ["acnxo", "igqh"])
hkki = Factor("hkki", ["bojkc", "phe"])
oju = Factor("oju", ["vsw", "xfg"])
### DERIVED FACTORS
##
def is_djawfc_clt(oju, hkki):
    return oju == hkki
def is_djawfc_pkadp(oju, hkki):
    return not is_djawfc_clt(oju, hkki)
djawfc = Factor("djawfc", [DerivedLevel("clt", WithinTrial(is_djawfc_clt, [oju, hkki])), DerivedLevel("pkadp", WithinTrial(is_djawfc_pkadp, [oju, hkki]))])
### EXPERIMENT
constraints = [AtLeastKInARow(4, mefc), MinimumTrials(27)]
crossing = [djawfc, hkki]
design=[loslz,odd,mefc,hkki,oju,djawfc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
