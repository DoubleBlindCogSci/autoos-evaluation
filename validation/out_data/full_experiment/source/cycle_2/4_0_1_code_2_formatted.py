### REGULAR FACTORS
hix = Factor("hix", ["ihhe", "apzae"])
ijkvct = Factor("ijkvct", ["fbww", "fna"])
mowgsv = Factor("mowgsv", ["ihhe", "apzae"])
axw = Factor("axw", ["fbww", "fna"])
### EXPERIMENT
constraints = [ExactlyKInARow(3, (ijkvct, "fbww"))]
crossing = [ijkvct, axw]
design=[hix,ijkvct,mowgsv,axw]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
