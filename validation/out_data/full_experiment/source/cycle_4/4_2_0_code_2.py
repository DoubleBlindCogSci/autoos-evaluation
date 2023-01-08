from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
npfih = Factor("npfih", ["zqc", "szrkc"])
ldtn = Factor("ldtn", ["eqq", "mcuj"])
olhm = Factor("olhm", ["zqc", "szrkc"])
vac = Factor("vac", ["eqq", "mcuj"])
def is_rnm_zsrr(olhm, npfih):
    return olhm == npfih
def is_rnm_ebnz(olhm, npfih):
    return not is_rnm_zsrr(olhm, npfih)
rnm = Factor("rnm", [DerivedLevel("zsrr", WithinTrial(is_rnm_zsrr, [olhm, npfih])), DerivedLevel("ebnz", WithinTrial(is_rnm_ebnz, [olhm, npfih]))])
def is_oelqby_njfk(vac, ldtn):
    return vac == ldtn
def is_oelqby_oaiui(vac, ldtn):
    return not is_oelqby_njfk(vac, ldtn)
oelqby = Factor("oelqby", [DerivedLevel("njfk", WithinTrial(is_oelqby_njfk, [vac, ldtn])), DerivedLevel("oaiui", WithinTrial(is_oelqby_oaiui, [vac, ldtn]))])
constraints = []
crossing = [ldtn, olhm]

design=[npfih,ldtn,olhm,vac,rnm,oelqby]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_0"))
