from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
chrlaq = Factor("chrlaq", ["tdmy", "jevqi"])
fbxkr = Factor("fbxkr", ["brsx", "soct"])
iuqbla = Factor("iuqbla", ["tdmy", "jevqi"])
mozm = Factor("mozm", ["brsx", "soct"])
def is_fjoa_icnyt(mozm, iuqbla):
    return mozm == iuqbla
def is_fjoa_ove(mozm, iuqbla):
    return not is_fjoa_icnyt(mozm, iuqbla)
fjoa= Factor("fjoa", [DerivedLevel("icnyt", WithinTrial(is_fjoa_icnyt, [mozm, iuqbla])), DerivedLevel("ove", WithinTrial(is_fjoa_ove, [mozm, iuqbla]))])
constraints = [AtMostKInARow(4, fjoa), AtLeastKInARow(4, fbxkr)]
crossing = [iuqbla, chrlaq]

design=[chrlaq,fbxkr,iuqbla,mozm,fjoa]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_2"))
