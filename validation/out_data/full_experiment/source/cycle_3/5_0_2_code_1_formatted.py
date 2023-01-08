### REGULAR FACTORS
oyi = Factor("oyi", ["cjtg", "hpmo"])
gxqk = Factor("gxqk", ["rfk", "usnhq"])
holhg = Factor("holhg", ["cjtg", "hpmo"])
wpl = Factor("wpl", ["rfk", "usnhq"])
ngp = Factor("ngp", ["qqk", "eqpc"])
### EXPERIMENT
design=[oyi,gxqk,holhg,wpl,ngp]
constraints=[MinimumTrials(16),AtMostKInARow(4, ngp)]
crossing=[gxqk,holhg]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
