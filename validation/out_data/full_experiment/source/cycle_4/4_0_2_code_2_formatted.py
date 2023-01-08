### REGULAR FACTORS
vbuipz = Factor("vbuipz", ["wkzx", "iuoqy"])
ilcgi = Factor("ilcgi", ["vkdwcr", "klerfi"])
ggw = Factor("ggw", ["wkzx", "iuoqy"])
dolfc = Factor("dolfc", ["vkdwcr", "klerfi"])
### EXPERIMENT
constraints = [AtMostKInARow(2, ggw), MinimumTrials(46)]
crossing = [ggw, vbuipz]
design=[vbuipz,ilcgi,ggw,dolfc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
