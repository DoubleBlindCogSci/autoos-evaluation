### REGULAR FACTORS
hix = Factor("hix", ["ihhe", "apzae"])
ijkvct = Factor("ijkvct", ["fbww", "fna"])
mowgsv = Factor("mowgsv", ["ihhe", "apzae"])
axw = Factor("axw", ["fbww", "fna"])
### EXPERIMENT
design=[hix,ijkvct,mowgsv,axw]
constraints=[ExactlyKInARow(3, ijkvct)]
crossing=[ijkvct,axw]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
