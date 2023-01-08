### REGULAR FACTORS
rffvf = Factor("rffvf", ["zfi", "rmut"])
xyxhz = Factor("xyxhz", ["qowuql", "tlat"])
tbgx = Factor("tbgx", ["zfi", "rmut"])
yds = Factor("yds", ["qowuql", "tlat"])
### EXPERIMENT
constraints = [AtLeastKInARow(4, tbgx), AtMostKInARow(4, xyxhz)]
crossing = [tbgx, xyxhz]
design=[rffvf,xyxhz,tbgx,yds]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
