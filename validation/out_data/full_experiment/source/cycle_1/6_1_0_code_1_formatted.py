### REGULAR FACTORS
ptxf = Factor("ptxf", ["nsmjwr", "iqbzt"])
fthd = Factor("fthd", ["fuezsy", "ddldqs"])
lln = Factor("lln", ["nsmjwr", "iqbzt"])
lfcap = Factor("lfcap", ["fuezsy", "ddldqs"])
tku = Factor("tku", ["qupefs", "nbo"])
rvpgn = Factor("rvpgn", ["pysk", "ihgxhj"])
### DERIVED FACTORS
##
def ihy (lfcap, fthd):
    return lfcap == fthd
def jfenxo (lfcap, fthd):
    return not ihy(lfcap, fthd)
hjkr = Factor("hjkr", [DerivedLevel("xwex", WithinTrial(ihy, [lfcap, fthd])), DerivedLevel("cidq", WithinTrial(jfenxo, [lfcap, fthd]))])
##
### EXPERIMENT
design=[hjkr,ptxf,fthd,lln,lfcap,tku,rvpgn]
constraints=[]
crossing=[fthd,tku]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
