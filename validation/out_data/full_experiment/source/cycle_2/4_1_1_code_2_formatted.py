### REGULAR FACTORS
bwiy = Factor("bwiy", ["nkk", "wpgc"])
duutsq = Factor("duutsq", ["kwt", "aovg"])
gjhyl = Factor("gjhyl", ["nkk", "wpgc"])
gkp = Factor("gkp", ["kwt", "aovg"])
### DERIVED FACTORS
##
def is_ulbw_ygc(gjhyl, duutsq):
    return gjhyl == duutsq
def is_ulbw_kuut(gjhyl, duutsq):
    return not is_ulbw_ygc(gjhyl, duutsq)
ulbw= Factor("ulbw", [DerivedLevel("ygc", WithinTrial(is_ulbw_ygc, [gjhyl, duutsq])), DerivedLevel("kuut", WithinTrial(is_ulbw_kuut, [gjhyl, duutsq]))])
### EXPERIMENT
constraints = [AtMostKInARow(4, bwiy)]
crossing = [ulbw, gkp]
design=[bwiy,duutsq,gjhyl,gkp]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
