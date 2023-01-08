### REGULAR FACTORS
vbuipz = Factor("vbuipz", ["wkzx", "iuoqy"])
ilcgi = Factor("ilcgi", ["vkdwcr", "klerfi"])
ggw = Factor("ggw", ["wkzx", "iuoqy"])
dolfc = Factor("dolfc", ["vkdwcr", "klerfi"])
### EXPERIMENT
design=[vbuipz,ilcgi,ggw,dolfc]
constraints=[AtMostKInARow(2, ggw),MinimumTrials(46)]
crossing=[ggw,vbuipz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
