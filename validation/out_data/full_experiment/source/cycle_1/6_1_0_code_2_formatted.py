### REGULAR FACTORS
ptxf = Factor("ptxf", ["nsmjwr", "iqbzt"])
fthd = Factor("fthd", ["fuezsy", "ddldqs"])
lln = Factor("lln", ["nsmjwr", "iqbzt"])
lfcap = Factor("lfcap", ["fuezsy", "ddldqs"])
tku = Factor("tku", ["qupefs", "nbo"])
rvpgn = Factor("rvpgn", ["pysk", "ihgxhj"])
### DERIVED FACTORS
##
def is_hjkr_xwex(lfcap, fthd):
    return lfcap == fthd
def is_hjkr_cidq(lfcap, fthd):
    return not is_hjkr_xwex(lfcap, fthd)
hjkr= Factor("hjkr", [DerivedLevel("xwex", WithinTrial(is_hjkr_xwex, [lfcap, fthd])), DerivedLevel("cidq", WithinTrial(is_hjkr_cidq, [lfcap, fthd]))])
### EXPERIMENT
constraints = []
crossing = [fthd, tku]
design=[ptxf,fthd,lln,lfcap,tku,rvpgn]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
