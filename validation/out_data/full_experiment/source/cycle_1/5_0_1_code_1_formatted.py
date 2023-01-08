### REGULAR FACTORS
unrxx = Factor("unrxx", ["juabnh", "gbnqm"])
vvdgwd = Factor("vvdgwd", ["ccwoqj", "zevijt"])
fbr = Factor("fbr", ["juabnh", "gbnqm"])
fqyzr = Factor("fqyzr", ["ccwoqj", "zevijt"])
qqgqvy = Factor("qqgqvy", ["jmterk", "ripcij"])
### EXPERIMENT
design=[unrxx,vvdgwd,fbr,fqyzr,qqgqvy]
constraints=[AtLeastKInARow(4, qqgqvy)]
crossing=[unrxx,fbr]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
