### REGULAR FACTORS
xsoc = Factor("xsoc", ["aick", "thojyk"])
qzjdvx = Factor("qzjdvx", ["orlug", "condlo"])
syz = Factor("syz", ["aick", "thojyk"])
qgx = Factor("qgx", ["orlug", "condlo"])
oubi = Factor("oubi", ["rnje", "wawxwx"])
### EXPERIMENT
constraints = [AtLeastKInARow(2, (qgx, "orlug")), ExactlyKInARow(2, (qzjdvx, "aick"))]
crossing = [qgx, syz]
design=[xsoc,qzjdvx,syz,qgx,oubi]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
