### REGULAR FACTORS
unrxx = Factor("unrxx", ["juabnh", "gbnqm"])
vvdgwd = Factor("vvdgwd", ["ccwoqj", "zevijt"])
fbr = Factor("fbr", ["juabnh", "gbnqm"])
fqyzr = Factor("fqyzr", ["ccwoqj", "zevijt"])
qqgqvy = Factor("qqgqvy", ["jmterk", "ripcij"])
### EXPERIMENT
constraints = [AtLeastKInARow(4, (qqgqvy, "jmterk"))]
crossing = [unrxx, fbr]
design=[unrxx,vvdgwd,fbr,fqyzr,qqgqvy]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
