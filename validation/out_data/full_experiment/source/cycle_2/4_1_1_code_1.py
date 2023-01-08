from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
bwiy = Factor("bwiy", ["nkk", "wpgc"])
duutsq = Factor("duutsq", ["kwt", "aovg"])
gjhyl = Factor("gjhyl", ["nkk", "wpgc"])
gkp = Factor("gkp", ["kwt", "aovg"])
def cff (gjhyl, duutsq):
    return gjhyl == duutsq
def xdfkpc (gjhyl, duutsq):
    return not cff(gjhyl, duutsq)
ulbw = Factor("ulbw", [DerivedLevel("ygc", WithinTrial(cff, [gjhyl, duutsq])), DerivedLevel("kuut", WithinTrial(xdfkpc, [gjhyl, duutsq]))])
design=[ulbw,bwiy,duutsq,gjhyl,gkp]
constraints=[AtMostKInARow(4, bwiy)]
crossing=[ulbw,gkp]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
