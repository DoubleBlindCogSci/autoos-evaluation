### REGULAR FACTORS
avum = Factor("avum", ["oybsg", "gtx"])
lzq = Factor("lzq", ["xrx", "vawzds"])
cxoc = Factor("cxoc", ["oybsg", "gtx"])
ukhrk = Factor("ukhrk", ["xrx", "vawzds"])
guphvz = Factor("guphvz", ["mmmq", "tcwyd"])
### DERIVED FACTORS
##
def ptzo (guphvz, lzq):
    return guphvz == lzq
def yukbie (guphvz, lzq):
    return not ptzo(guphvz, lzq)
ussdf = Factor("ussdf", [DerivedLevel("kcln", WithinTrial(ptzo, [guphvz, lzq])), DerivedLevel("waekbz", WithinTrial(yukbie, [guphvz, lzq]))])
##
### EXPERIMENT
design=[ussdf,avum,lzq,cxoc,ukhrk,guphvz]
constraints=[AtMostKInARow(3, ukhrk)]
crossing=[avum,guphvz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
