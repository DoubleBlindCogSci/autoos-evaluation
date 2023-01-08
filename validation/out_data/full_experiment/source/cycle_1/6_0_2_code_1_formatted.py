### REGULAR FACTORS
pohbz = Factor("pohbz", ["bpev", "kiujoc"])
edcx = Factor("edcx", ["tyc", "yunio"])
yoma = Factor("yoma", ["bpev", "kiujoc"])
wmhjq = Factor("wmhjq", ["tyc", "yunio"])
wegj = Factor("wegj", ["mbg", "xpjjgv"])
fdhif = Factor("fdhif", ["atcbho", "ziqlyq"])
### EXPERIMENT
design=[pohbz,edcx,yoma,wmhjq,wegj,fdhif]
constraints=[MinimumTrials(50),AtLeastKInARow(3, wegj)]
crossing=[yoma,edcx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
