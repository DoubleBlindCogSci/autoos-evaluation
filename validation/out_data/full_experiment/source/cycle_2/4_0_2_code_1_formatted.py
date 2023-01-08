### REGULAR FACTORS
rffvf = Factor("rffvf", ["zfi", "rmut"])
xyxhz = Factor("xyxhz", ["qowuql", "tlat"])
tbgx = Factor("tbgx", ["zfi", "rmut"])
yds = Factor("yds", ["qowuql", "tlat"])
### EXPERIMENT
design=[rffvf,xyxhz,tbgx,yds]
constraints=[AtLeastKInARow(4, tbgx),AtMostKInARow(4, xyxhz)]
crossing=[tbgx,xyxhz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
