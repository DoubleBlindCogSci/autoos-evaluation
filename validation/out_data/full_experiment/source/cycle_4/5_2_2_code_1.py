from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ihaxo = Factor("ihaxo", ["nebj", "gqov"])
mwabx = Factor("mwabx", ["upfna", "qnn"])
drfsq = Factor("drfsq", ["nebj", "gqov"])
wwviw = Factor("wwviw", ["upfna", "qnn"])
ddx = Factor("ddx", ["oesdd", "cgcxdg"])
def rkif (wwviw, ddx):
    return wwviw == ddx
def dmlds (wwviw, ddx):
    return not rkif(wwviw, ddx)
mehm = Factor("mehm", [DerivedLevel("onat", WithinTrial(rkif, [wwviw, ddx])), DerivedLevel("zbtzh", WithinTrial(dmlds, [wwviw, ddx]))])
def xjcy (drfsq, ihaxo):
    return drfsq == ihaxo
def hlh (drfsq, ihaxo):
    return not xjcy(drfsq, ihaxo)
trtz = Factor("trtz", [DerivedLevel("itvon", WithinTrial(xjcy, [drfsq, ihaxo])), DerivedLevel("cuvewk", WithinTrial(hlh, [drfsq, ihaxo]))])
design=[mehm,trtz,ihaxo,mwabx,drfsq,wwviw,ddx]
constraints=[ExactlyKInARow(3, trtz),AtLeastKInARow(2, trtz)]
crossing=[wwviw,trtz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_2"))
