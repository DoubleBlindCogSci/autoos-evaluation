### REGULAR FACTORS
pohbz = Factor("pohbz", ["bpev", "kiujoc"])
edcx = Factor("edcx", ["tyc", "yunio"])
yoma = Factor("yoma", ["bpev", "kiujoc"])
wmhjq = Factor("wmhjq", ["tyc", "yunio"])
wegj = Factor("wegj", ["mbg", "xpjjgv"])
fdhif = Factor("fdhif", ["atcbho", "ziqlyq"])
### EXPERIMENT
constraints = [AtLeastKInARow(3, (fdhif, "atcbho")), MinimumTrials(50)]
crossing = [yoma, edcx]
design=[pohbz,edcx,yoma,wmhjq,wegj,fdhif]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
