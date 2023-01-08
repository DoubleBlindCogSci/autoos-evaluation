### REGULAR FACTORS
lbb = Factor("lbb", ["yzmmfa", "arhbc"])
sndpyx = Factor("sndpyx", ["utxa", "raqlqp"])
dwbg = Factor("dwbg", ["yzmmfa", "arhbc"])
wrzorv = Factor("wrzorv", ["utxa", "raqlqp"])
luu = Factor("luu", ["gqiz", "qjv"])
### EXPERIMENT
constraints = [AtMostKInARow(3, luu)]
crossing = [wrzorv, luu]
design=[lbb,sndpyx,dwbg,wrzorv,luu]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
