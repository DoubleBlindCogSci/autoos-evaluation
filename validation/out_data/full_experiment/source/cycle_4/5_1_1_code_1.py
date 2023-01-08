from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
avum = Factor("avum", ["oybsg", "gtx"])
lzq = Factor("lzq", ["xrx", "vawzds"])
cxoc = Factor("cxoc", ["oybsg", "gtx"])
ukhrk = Factor("ukhrk", ["xrx", "vawzds"])
guphvz = Factor("guphvz", ["mmmq", "tcwyd"])
def ptzo (guphvz, lzq):
    return guphvz == lzq
def yukbie (guphvz, lzq):
    return not ptzo(guphvz, lzq)
ussdf = Factor("ussdf", [DerivedLevel("kcln", WithinTrial(ptzo, [guphvz, lzq])), DerivedLevel("waekbz", WithinTrial(yukbie, [guphvz, lzq]))])
design=[ussdf,avum,lzq,cxoc,ukhrk,guphvz]
constraints=[AtMostKInARow(3, ukhrk)]
crossing=[avum,guphvz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
