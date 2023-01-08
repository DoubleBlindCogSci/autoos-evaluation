### REGULAR FACTORS
ftg = Factor("ftg", ["nqxlo", "iqtp"])
cdt = Factor("cdt", ["pcm", "hqiju"])
wgrk = Factor("wgrk", ["nqxlo", "iqtp"])
buvqha = Factor("buvqha", ["pcm", "hqiju"])
### DERIVED FACTORS
##
def nfrrw (cdt, wgrk):
    return cdt == wgrk
def jvymc (cdt, wgrk):
    return not nfrrw(cdt, wgrk)
gcu = Factor("gcu", [DerivedLevel("wziqu", WithinTrial(nfrrw, [cdt, wgrk])), DerivedLevel("slbd", WithinTrial(jvymc, [cdt, wgrk]))])
### EXPERIMENT
design=[gcu,ftg,cdt,wgrk,buvqha]
constraints=[MinimumTrials(35),ExactlyKInARow(3, gcu)]
crossing=[ftg,gcu]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
