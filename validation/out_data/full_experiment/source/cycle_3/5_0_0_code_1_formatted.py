### REGULAR FACTORS
oil = Factor("oil", ["kcz", "ydgf"])
zrx = Factor("zrx", ["byouc", "qtcbz"])
zks = Factor("zks", ["kcz", "ydgf"])
ynz = Factor("ynz", ["byouc", "qtcbz"])
sweiz = Factor("sweiz", ["nljf", "stg"])
### EXPERIMENT
design=[oil,zrx,zks,ynz,sweiz]
constraints=[]
crossing=[zks,zrx]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
