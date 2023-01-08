### REGULAR FACTORS
nzcbj = Factor("nzcbj", ["qxclap", "ggnefj"])
brdzmk = Factor("brdzmk", ["xhra", "uhllj"])
pvza = Factor("pvza", ["qxclap", "ggnefj"])
bglcc = Factor("bglcc", ["xhra", "uhllj"])
### EXPERIMENT
constraints = []
crossing = [nzcbj, brdzmk]
design=[nzcbj,brdzmk,pvza,bglcc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
