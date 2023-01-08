from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
wbr = Factor("wbr", ["ntmsnw", "fouy"])
wlw = Factor("wlw", ["ycpahd", "eydki"])
pcnmlg = Factor("pcnmlg", ["ntmsnw", "fouy"])
tow = Factor("tow", ["ycpahd", "eydki"])
def is_srcywn_icthpl(wlw, tow):
    return wlw == tow
def is_srcywn_txdzmf(wlw, tow):
    return not is_srcywn_icthpl(wlw, tow)
srcywn= Factor("srcywn", [DerivedLevel("icthpl", WithinTrial(is_srcywn_icthpl, [wlw, tow])), DerivedLevel("txdzmf", WithinTrial(is_srcywn_txdzmf, [wlw, tow]))])
constraints = []
crossing = [wbr, wlw]

design=[wbr,wlw,pcnmlg,tow,srcywn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_0"))
