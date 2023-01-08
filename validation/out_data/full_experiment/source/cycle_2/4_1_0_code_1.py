from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
wbr = Factor("wbr", ["ntmsnw", "fouy"])
wlw = Factor("wlw", ["ycpahd", "eydki"])
pcnmlg = Factor("pcnmlg", ["ntmsnw", "fouy"])
tow = Factor("tow", ["ycpahd", "eydki"])
def ijfamm (wlw, tow):
    return wlw == tow
def oxrtfi (wlw, tow):
    return not ijfamm(wlw, tow)
srcywn = Factor("srcywn", [DerivedLevel("icthpl", WithinTrial(ijfamm, [wlw, tow])), DerivedLevel("txdzmf", WithinTrial(oxrtfi, [wlw, tow]))])
design=[srcywn,wbr,wlw,pcnmlg,tow]
constraints=[]
crossing=[wbr,wlw]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
