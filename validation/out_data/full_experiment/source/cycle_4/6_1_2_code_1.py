from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
snat = Factor("snat", ["pkijs", "krrj"])
kaqka = Factor("kaqka", ["inqo", "qggwd"])
lvisj = Factor("lvisj", ["pkijs", "krrj"])
gqw = Factor("gqw", ["inqo", "qggwd"])
wkqe = Factor("wkqe", ["cpar", "pcfsm"])
pyoyje = Factor("pyoyje", ["yejf", "aupzma"])
def fdr (lvisj, pyoyje):
    return lvisj == pyoyje
def euiuag (lvisj, pyoyje):
    return not fdr(lvisj, pyoyje)
hjip = Factor("hjip", [DerivedLevel("tutcm", WithinTrial(fdr, [lvisj, pyoyje])), DerivedLevel("micqz", WithinTrial(euiuag, [lvisj, pyoyje]))])
design=[hjip,snat,kaqka,lvisj,gqw,wkqe,pyoyje]
constraints=[ExactlyKInARow(4, wkqe),AtMostKInARow(2, snat)]
crossing=[kaqka,hjip]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_2"))
