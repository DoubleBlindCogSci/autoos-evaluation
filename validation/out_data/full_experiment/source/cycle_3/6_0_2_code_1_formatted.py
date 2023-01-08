### REGULAR FACTORS
kqs = Factor("kqs", ["tqou", "zqh"])
xmy = Factor("xmy", ["nepkz", "ntiaq"])
mvcr = Factor("mvcr", ["tqou", "zqh"])
bzowuv = Factor("bzowuv", ["nepkz", "ntiaq"])
abkw = Factor("abkw", ["uil", "kes"])
zeqtq = Factor("zeqtq", ["nhzv", "npofit"])
### EXPERIMENT
design=[kqs,xmy,mvcr,bzowuv,abkw,zeqtq]
constraints=[AtLeastKInARow(3, abkw),AtMostKInARow(2, bzowuv)]
crossing=[mvcr,xmy]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
