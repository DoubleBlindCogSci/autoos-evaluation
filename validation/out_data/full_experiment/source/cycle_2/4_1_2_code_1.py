from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
chrlaq = Factor("chrlaq", ["tdmy", "jevqi"])
fbxkr = Factor("fbxkr", ["brsx", "soct"])
iuqbla = Factor("iuqbla", ["tdmy", "jevqi"])
mozm = Factor("mozm", ["brsx", "soct"])
def stkcrb (mozm, iuqbla):
    return mozm == iuqbla
def qxk (mozm, iuqbla):
    return not stkcrb(mozm, iuqbla)
fjoa = Factor("fjoa", [DerivedLevel("icnyt", WithinTrial(stkcrb, [mozm, iuqbla])), DerivedLevel("ove", WithinTrial(qxk, [mozm, iuqbla]))])
design=[fjoa,chrlaq,fbxkr,iuqbla,mozm]
constraints=[AtMostKInARow(4, fjoa),ExactlyKInARow(4, fbxkr)]
crossing=[iuqbla,chrlaq]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_2"))
