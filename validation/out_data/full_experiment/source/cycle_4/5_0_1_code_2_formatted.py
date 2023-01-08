### REGULAR FACTORS
opth = Factor("opth", ["cupxsi", "jehney"])
jtwon = Factor("jtwon", ["nupd", "tkkn"])
qgaatu = Factor("qgaatu", ["cupxsi", "jehney"])
cnekt = Factor("cnekt", ["nupd", "tkkn"])
ryuvgo = Factor("ryuvgo", ["hsm", "ghlii"])
### EXPERIMENT
constraints = [ExactlyKInARow(4, (cnekt, "nupd"))]
crossing = [cnekt, jtwon]
design=[opth,jtwon,qgaatu,cnekt,ryuvgo]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
