### REGULAR FACTORS
bwiy = Factor("bwiy", ["nkk", "wpgc"])
duutsq = Factor("duutsq", ["kwt", "aovg"])
gjhyl = Factor("gjhyl", ["nkk", "wpgc"])
gkp = Factor("gkp", ["kwt", "aovg"])
### DERIVED FACTORS
##
def cff (gjhyl, duutsq):
    return gjhyl == duutsq
def xdfkpc (gjhyl, duutsq):
    return not cff(gjhyl, duutsq)
ulbw = Factor("ulbw", [DerivedLevel("ygc", WithinTrial(cff, [gjhyl, duutsq])), DerivedLevel("kuut", WithinTrial(xdfkpc, [gjhyl, duutsq]))])
### EXPERIMENT
design=[ulbw,bwiy,duutsq,gjhyl,gkp]
constraints=[AtMostKInARow(4, bwiy)]
crossing=[ulbw,gkp]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
