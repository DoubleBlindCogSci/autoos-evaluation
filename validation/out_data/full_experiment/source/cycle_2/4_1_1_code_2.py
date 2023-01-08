from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
bwiy = Factor("bwiy", ["nkk", "wpgc"])
duutsq = Factor("duutsq", ["kwt", "aovg"])
gjhyl = Factor("gjhyl", ["nkk", "wpgc"])
gkp = Factor("gkp", ["kwt", "aovg"])
def is_ulbw_ygc(gjhyl, duutsq):
    return gjhyl == duutsq
def is_ulbw_kuut(gjhyl, duutsq):
    return not is_ulbw_ygc(gjhyl, duutsq)
ulbw= Factor("ulbw", [DerivedLevel("ygc", WithinTrial(is_ulbw_ygc, [gjhyl, duutsq])), DerivedLevel("kuut", WithinTrial(is_ulbw_kuut, [gjhyl, duutsq]))])
constraints = [AtMostKInARow(4, bwiy)]
crossing = [ulbw, gkp]

design=[bwiy,duutsq,gjhyl,gkp, ulbw]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))
