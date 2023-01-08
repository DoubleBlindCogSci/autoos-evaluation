from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
avum = Factor("avum", ["oybsg", "gtx"])
lzq = Factor("lzq", ["xrx", "vawzds"])
cxoc = Factor("cxoc", ["oybsg", "gtx"])
ukhrk = Factor("ukhrk", ["xrx", "vawzds"])
guphvz = Factor("guphvz", ["mmmq", "tcwyd"])
def is_ussdf_kcln(guphvz, lzq):
    return guphvz == lzq
def is_ussdf_waekbz(guphvz, lzq):
    return not is_ussdf_kcln(guphvz, lzq)
ussdf = Factor("ussdf", [DerivedLevel("kcln", WithinTrial(is_ussdf_kcln, [guphvz, lzq])), DerivedLevel("waekbz", WithinTrial(is_ussdf_waekbz, [guphvz, lzq]))])
constraints = [AtMostKInARow(3, ukhrk)]
crossing = [avum, guphvz]

design=[avum,lzq,cxoc,ukhrk,guphvz,ussdf]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_1"))
