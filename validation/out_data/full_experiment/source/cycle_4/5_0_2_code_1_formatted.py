### REGULAR FACTORS
muv = Factor("muv", ["hdbuig", "xtfto"])
xqnr = Factor("xqnr", ["razmc", "byv"])
rggn = Factor("rggn", ["hdbuig", "xtfto"])
xhstdg = Factor("xhstdg", ["razmc", "byv"])
vezedn = Factor("vezedn", ["osby", "tkvl"])
### EXPERIMENT
design=[muv,xqnr,rggn,xhstdg,vezedn]
constraints=[AtLeastKInARow(2, muv),ExactlyKInARow(4, rggn)]
crossing=[rggn,vezedn]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
