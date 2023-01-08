### REGULAR FACTORS
xti = Factor("xti", ["hdlc", "nodrfn"])
nzuufr = Factor("nzuufr", ["bev", "vbequ"])
bxk = Factor("bxk", ["hdlc", "nodrfn"])
gokv = Factor("gokv", ["bev", "vbequ"])
### EXPERIMENT
design=[xti,nzuufr,bxk,gokv]
constraints=[AtMostKInARow(2, nzuufr)]
crossing=[gokv,nzuufr]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
