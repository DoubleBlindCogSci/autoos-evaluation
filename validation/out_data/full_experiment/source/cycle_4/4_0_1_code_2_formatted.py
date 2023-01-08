### REGULAR FACTORS
dpgpee = Factor("dpgpee", ["griwc", "rcttpe"])
sbbw = Factor("sbbw", ["voq", "iatd"])
cbglx = Factor("cbglx", ["griwc", "rcttpe"])
kxru = Factor("kxru", ["voq", "iatd"])
### EXPERIMENT
constraints = [MinimumTrials(31)]
crossing = [cbglx, dpgpee]
design=[dpgpee,sbbw,cbglx,kxru]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
