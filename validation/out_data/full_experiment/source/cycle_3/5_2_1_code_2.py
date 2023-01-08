from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
ckt = Factor("ckt", ["ypkjl", "yitd"])
smu = Factor("smu", ["xbeqh", "albh"])
psn = Factor("psn", ["ypkjl", "yitd"])
tpk = Factor("tpk", ["xbeqh", "albh"])
eyzwf = Factor("eyzwf", ["oyjyxm", "rsk"])
def is_erm_qhb(smu, psn):
    return smu == psn
def is_erm_hqdkzn(smu, psn):
    return not is_erm_qhb(smu, psn)
erm = Factor("erm", [DerivedLevel("qhb", WithinTrial(is_erm_qhb, [smu, psn])), DerivedLevel("hqdkzn", WithinTrial(is_erm_hqdkzn, [smu, psn]))])
def is_rrlxc_mpm(eyzwf, tpk):
    return eyzwf == tpk
def is_rrlxc_gyei(eyzwf, tpk):
    return not is_rrlxc_mpm(eyzwf, tpk)
rrlxc = Factor("rrlxc", [DerivedLevel("mpm", WithinTrial(is_rrlxc_mpm, [eyzwf, tpk])), DerivedLevel("gyei", WithinTrial(is_rrlxc_gyei, [eyzwf, tpk]))])
constraints = [ExactlyKInARow(4, (psn, "ypkjl"))]
crossing = [smu, psn]

design=[ckt,smu,psn,tpk,eyzwf,erm,rrlxc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_1"))
