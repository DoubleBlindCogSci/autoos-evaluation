### REGULAR FACTORS
hzss = Factor("hzss", ["ujnts", "jkw"])
kdzg = Factor("kdzg", ["xdrmxs", "asdgvm"])
axn = Factor("axn", ["ujnts", "jkw"])
cvf = Factor("cvf", ["xdrmxs", "asdgvm"])
djjd = Factor("djjd", ["vymblj", "sii"])
### EXPERIMENT
constraints = [AtLeastKInARow(4, (axn, "ujnts"))]
crossing = [cvf, hzss]
design=[hzss,kdzg,axn,cvf,djjd]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
