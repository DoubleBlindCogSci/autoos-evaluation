### REGULAR FACTORS
dgizf = Factor("dgizf", ["omekh", "jkt"])
imjtfj = Factor("imjtfj", ["gkhdp", "fyjb"])
amui = Factor("amui", ["omekh", "jkt"])
paanhe = Factor("paanhe", ["gkhdp", "fyjb"])
uirzmz = Factor("uirzmz", ["tdo", "gwtex"])
qhpc = Factor("qhpc", ["esaypj", "bps"])
### EXPERIMENT
design=[dgizf,imjtfj,amui,paanhe,uirzmz,qhpc]
constraints=[AtLeastKInARow(4, uirzmz)]
crossing=[dgizf,qhpc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
