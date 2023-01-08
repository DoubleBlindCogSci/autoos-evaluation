### REGULAR FACTORS
loslz = Factor("loslz", ["acnxo", "igqh"])
odd = Factor("odd", ["bojkc", "phe"])
mefc = Factor("mefc", ["acnxo", "igqh"])
hkki = Factor("hkki", ["bojkc", "phe"])
oju = Factor("oju", ["vsw", "xfg"])
### DERIVED FACTORS
##
def sko (oju, hkki):
    return oju == hkki
def ynim (oju, hkki):
    return not sko(oju, hkki)
djawfc = Factor("djawfc", [DerivedLevel("clt", WithinTrial(sko, [oju, hkki])), DerivedLevel("pkadp", WithinTrial(ynim, [oju, hkki]))])
##
### EXPERIMENT
design=[djawfc,loslz,odd,mefc,hkki,oju]
constraints=[MinimumTrials(27),AtLeastKInARow(4, mefc)]
crossing=[djawfc,hkki]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
