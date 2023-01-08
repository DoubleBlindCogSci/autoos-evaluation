### REGULAR FACTORS
ubgs = Factor("ubgs", ["tddsj", "pru"])
htydch = Factor("htydch", ["lsqmxp", "xuukpx"])
tclwi = Factor("tclwi", ["tddsj", "pru"])
kvxse = Factor("kvxse", ["lsqmxp", "xuukpx"])
icb = Factor("icb", ["qsc", "fjil"])
rfsofe = Factor("rfsofe", ["zcu", "gzr"])
### EXPERIMENT
design=[ubgs,htydch,tclwi,kvxse,icb,rfsofe]
constraints=[]
crossing=[kvxse,icb]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
