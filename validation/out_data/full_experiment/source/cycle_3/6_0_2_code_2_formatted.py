### REGULAR FACTORS
kqs = Factor("kqs", ["tqou", "zqh"])
xmy = Factor("xmy", ["nepkz", "ntiaq"])
mvcr = Factor("mvcr", ["tqou", "zqh"])
bzowuv = Factor("bzowuv", ["nepkz", "ntiaq"])
abkw = Factor("abkw", ["uil", "kes"])
zeqtq = Factor("zeqtq", ["nhzv", "npofit"])
### EXPERIMENT
constraints = [AtLeastKInARow(3, (zeqtq, "nhzv")), AtMostKInARow(2, (zeqtq, "nhzv"))]
crossing = [mvcr, xmy]
design=[kqs,xmy,mvcr,bzowuv,abkw,zeqtq]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
