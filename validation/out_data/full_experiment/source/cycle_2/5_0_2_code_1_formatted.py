### REGULAR FACTORS
xsoc = Factor("xsoc", ["aick", "thojyk"])
qzjdvx = Factor("qzjdvx", ["orlug", "condlo"])
syz = Factor("syz", ["aick", "thojyk"])
qgx = Factor("qgx", ["orlug", "condlo"])
oubi = Factor("oubi", ["rnje", "wawxwx"])
### EXPERIMENT
design=[xsoc,qzjdvx,syz,qgx,oubi]
constraints=[AtLeastKInARow(2, qgx),ExactlyKInARow(2, qzjdvx)]
crossing=[qgx,syz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
