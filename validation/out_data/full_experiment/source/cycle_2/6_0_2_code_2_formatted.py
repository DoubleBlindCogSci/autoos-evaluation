### REGULAR FACTORS
fihow = Factor("fihow", ["jppw", "ncs"])
xck = Factor("xck", ["tvtou", "ugknb"])
ezqy = Factor("ezqy", ["jppw", "ncs"])
hqwon = Factor("hqwon", ["tvtou", "ugknb"])
chs = Factor("chs", ["tlyj", "fbf"])
pxaz = Factor("pxaz", ["bfdnum", "nlo"])
### EXPERIMENT
constraints = [AtLeastKInARow(4, chs), AtMostKInARow(2, pxaz)]
crossing = [fihow, pxaz]
design=[fihow,xck,ezqy,hqwon,chs,pxaz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
