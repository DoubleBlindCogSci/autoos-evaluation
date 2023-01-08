### REGULAR FACTORS
opth = Factor("opth", ["cupxsi", "jehney"])
jtwon = Factor("jtwon", ["nupd", "tkkn"])
qgaatu = Factor("qgaatu", ["cupxsi", "jehney"])
cnekt = Factor("cnekt", ["nupd", "tkkn"])
ryuvgo = Factor("ryuvgo", ["hsm", "ghlii"])
### EXPERIMENT
design=[opth,jtwon,qgaatu,cnekt,ryuvgo]
constraints=[ExactlyKInARow(4, cnekt)]
crossing=[cnekt,jtwon]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
