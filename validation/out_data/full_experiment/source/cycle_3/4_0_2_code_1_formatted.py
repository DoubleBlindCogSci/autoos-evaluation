### REGULAR FACTORS
xllver = Factor("xllver", ["kdzk", "yea"])
isvnwz = Factor("isvnwz", ["egcg", "vmymn"])
ayptso = Factor("ayptso", ["kdzk", "yea"])
ayupup = Factor("ayupup", ["egcg", "vmymn"])
### EXPERIMENT
design=[xllver,isvnwz,ayptso,ayupup]
constraints=[MinimumTrials(60),ExactlyKInARow(4, ayptso)]
crossing=[ayptso,ayupup]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
