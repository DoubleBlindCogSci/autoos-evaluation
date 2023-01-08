### REGULAR FACTORS
hzss = Factor("hzss", ["ujnts", "jkw"])
kdzg = Factor("kdzg", ["xdrmxs", "asdgvm"])
axn = Factor("axn", ["ujnts", "jkw"])
cvf = Factor("cvf", ["xdrmxs", "asdgvm"])
djjd = Factor("djjd", ["vymblj", "sii"])
### EXPERIMENT
design=[hzss,kdzg,axn,cvf,djjd]
constraints=[AtLeastKInARow(4, axn)]
crossing=[cvf,hzss]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
