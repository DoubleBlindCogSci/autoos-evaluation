### REGULAR FACTORS
avum = Factor("avum", ["oybsg", "gtx"])
lzq = Factor("lzq", ["xrx", "vawzds"])
cxoc = Factor("cxoc", ["oybsg", "gtx"])
ukhrk = Factor("ukhrk", ["xrx", "vawzds"])
guphvz = Factor("guphvz", ["mmmq", "tcwyd"])
### DERIVED FACTORS
##
def is_ussdf_kcln(guphvz, lzq):
    return guphvz == lzq
def is_ussdf_waekbz(guphvz, lzq):
    return not is_ussdf_kcln(guphvz, lzq)
ussdf = Factor("ussdf", [DerivedLevel("kcln", WithinTrial(is_ussdf_kcln, [guphvz, lzq])), DerivedLevel("waekbz", WithinTrial(is_ussdf_waekbz, [guphvz, lzq]))])
### EXPERIMENT
constraints = [AtMostKInARow(3, ukhrk)]
crossing = [avum, guphvz]
design=[avum,lzq,cxoc,ukhrk,guphvz,ussdf]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
