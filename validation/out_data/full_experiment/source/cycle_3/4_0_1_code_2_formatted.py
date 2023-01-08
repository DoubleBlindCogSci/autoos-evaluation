### REGULAR FACTORS
bvtai = Factor("bvtai", ["pvuel", "slfm"])
lembv = Factor("lembv", ["wfibz", "tryd"])
tfo = Factor("tfo", ["pvuel", "slfm"])
jerk = Factor("jerk", ["wfibz", "tryd"])
### EXPERIMENT
constraints = [MinimumTrials(58)]
crossing = [tfo, bvtai]
design=[bvtai,lembv,tfo,jerk]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
