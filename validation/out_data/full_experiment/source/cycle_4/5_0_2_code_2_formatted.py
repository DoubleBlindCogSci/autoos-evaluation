### REGULAR FACTORS
muv = Factor("muv", ["hdbuig", "xtfto"])
xqnr = Factor("xqnr", ["razmc", "byv"])
rggn = Factor("rggn", ["hdbuig", "xtfto"])
xhstdg = Factor("xhstdg", ["razmc", "byv"])
vezedn = Factor("vezedn", ["osby", "tkvl"])
### EXPERIMENT
constraints = [AtLeastKInARow(2, (muv, "hdbuig")), ExactlyKInARow(4, (rggn, "hdbuig"))]
crossing = [rggn, vezedn]
design=[muv,xqnr,rggn,xhstdg,vezedn]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
