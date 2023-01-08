from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ckt = Factor("ckt", ["ypkjl", "yitd"])
smu = Factor("smu", ["xbeqh", "albh"])
psn = Factor("psn", ["ypkjl", "yitd"])
tpk = Factor("tpk", ["xbeqh", "albh"])
eyzwf = Factor("eyzwf", ["oyjyxm", "rsk"])
def fardqu (smu, psn):
    return smu == psn
def tpormi (smu, psn):
    return not fardqu(smu, psn)
erm = Factor("erm", [DerivedLevel("qhb", WithinTrial(fardqu, [smu, psn])), DerivedLevel("hqdkzn", WithinTrial(tpormi, [smu, psn]))])
def cue (eyzwf, tpk):
    return eyzwf == tpk
def kdoxm (eyzwf, tpk):
    return not cue(eyzwf, tpk)
rrlxc = Factor("rrlxc", [DerivedLevel("mpm", WithinTrial(cue, [eyzwf, tpk])), DerivedLevel("gyei", WithinTrial(kdoxm, [eyzwf, tpk]))])
design=[erm,rrlxc,ckt,smu,psn,tpk,eyzwf]
constraints=[ExactlyKInARow(4, tpk)]
crossing=[smu,psn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
