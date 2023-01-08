### REGULAR FACTORS
qgplsu = Factor("qgplsu", ["pboibu", "zqdel"])
jjssm = Factor("jjssm", ["riesgx", "mxl"])
xaqd = Factor("xaqd", ["pboibu", "zqdel"])
utkb = Factor("utkb", ["riesgx", "mxl"])
nsmo = Factor("nsmo", ["zaxwi", "zews"])
qpgyns = Factor("qpgyns", ["dha", "upj"])
### EXPERIMENT
design=[qgplsu,jjssm,xaqd,utkb,nsmo,qpgyns]
constraints=[AtLeastKInARow(4, qpgyns)]
crossing=[qpgyns,nsmo]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
