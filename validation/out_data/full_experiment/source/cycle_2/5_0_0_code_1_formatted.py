### REGULAR FACTORS
zsin = Factor("zsin", ["keora", "obefln"])
zyf = Factor("zyf", ["vxcn", "vwxjol"])
psi = Factor("psi", ["keora", "obefln"])
tejntn = Factor("tejntn", ["vxcn", "vwxjol"])
hir = Factor("hir", ["hjsh", "aaba"])
### EXPERIMENT
design=[zsin,zyf,psi,tejntn,hir]
constraints=[]
crossing=[tejntn,hir]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
