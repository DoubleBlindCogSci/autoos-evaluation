### REGULAR FACTORS
xllver = Factor("xllver", ["kdzk", "yea"])
isvnwz = Factor("isvnwz", ["egcg", "vmymn"])
ayptso = Factor("ayptso", ["kdzk", "yea"])
ayupup = Factor("ayupup", ["egcg", "vmymn"])
### EXPERIMENT
constraints = [AtLeastKInARow(4, (ayptso, "egcg")), MinimumTrials(60)]
crossing = [ayptso, ayupup]
design=[xllver,isvnwz,ayptso,ayupup]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
