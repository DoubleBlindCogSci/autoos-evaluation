### REGULAR FACTORS
ftg = Factor("ftg", ["nqxlo", "iqtp"])
cdt = Factor("cdt", ["pcm", "hqiju"])
wgrk = Factor("wgrk", ["nqxlo", "iqtp"])
buvqha = Factor("buvqha", ["pcm", "hqiju"])
### DERIVED FACTORS
##
def is_gcu_wziqu(cdt, wgrk):
    return cdt == wgrk
def is_gcu_slbd(cdt, wgrk):
    return not is_gcu_wziqu(cdt, wgrk)
gcu = Factor("gcu", [DerivedLevel("wziqu", WithinTrial(is_gcu_wziqu, [cdt, wgrk])), DerivedLevel("slbd", WithinTrial(is_gcu_slbd, [cdt, wgrk]))])
### EXPERIMENT
constraints = [MinimumTrials(35), ExactlyK(3, (gcu, "wziqu"))]
crossing = [ftg, gcu]
design=[ftg,cdt,wgrk,buvqha,gcu]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
