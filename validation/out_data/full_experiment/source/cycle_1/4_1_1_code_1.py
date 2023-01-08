from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ozffyg = Factor("ozffyg", ["ktpg", "ezgdye"])
eor = Factor("eor", ["bvwt", "odzvfn"])
ulmvu = Factor("ulmvu", ["ktpg", "ezgdye"])
ydyizj = Factor("ydyizj", ["bvwt", "odzvfn"])
def vyt (eor, ydyizj):
    return eor == ydyizj
def zfu (eor, ydyizj):
    return not vyt(eor, ydyizj)
vnud = Factor("vnud", [DerivedLevel("cmru", WithinTrial(vyt, [eor, ydyizj])), DerivedLevel("hjfu", WithinTrial(zfu, [eor, ydyizj]))])
design=[vnud,ozffyg,eor,ulmvu,ydyizj]
constraints=[AtMostKInARow(3, vnud)]
crossing=[ulmvu,vnud]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_1_1"))
