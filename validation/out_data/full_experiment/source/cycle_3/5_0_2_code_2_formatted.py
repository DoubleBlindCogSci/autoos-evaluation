### REGULAR FACTORS
oyi = Factor("oyi", ["cjtg", "hpmo"])
gxqk = Factor("gxqk", ["rfk", "usnhq"])
holhg = Factor("holhg", ["cjtg", "hpmo"])
wpl = Factor("wpl", ["rfk", "usnhq"])
ngp = Factor("ngp", ["qqk", "eqpc"])
### EXPERIMENT
constraints = [AtMostKInARow(4, ngp), MinimumTrials(16)]
crossing = [gxqk, holhg]
design=[oyi,gxqk,holhg,wpl,ngp]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
