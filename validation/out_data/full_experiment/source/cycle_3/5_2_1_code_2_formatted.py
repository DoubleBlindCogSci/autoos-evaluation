### REGULAR FACTORS
ckt = Factor("ckt", ["ypkjl", "yitd"])
smu = Factor("smu", ["xbeqh", "albh"])
psn = Factor("psn", ["ypkjl", "yitd"])
tpk = Factor("tpk", ["xbeqh", "albh"])
eyzwf = Factor("eyzwf", ["oyjyxm", "rsk"])
### DERIVED FACTORS
##
def is_erm_qhb(smu, psn):
    return smu == psn
def is_erm_hqdkzn(smu, psn):
    return not is_erm_qhb(smu, psn)
erm = Factor("erm", [DerivedLevel("qhb", WithinTrial(is_erm_qhb, [smu, psn])), DerivedLevel("hqdkzn", WithinTrial(is_erm_hqdkzn, [smu, psn]))])
##
def is_rrlxc_mpm(eyzwf, tpk):
    return eyzwf == tpk
def is_rrlxc_gyei(eyzwf, tpk):
    return not is_rrlxc_mpm(eyzwf, tpk)
rrlxc = Factor("rrlxc", [DerivedLevel("mpm", WithinTrial(is_rrlxc_mpm, [eyzwf, tpk])), DerivedLevel("gyei", WithinTrial(is_rrlxc_gyei, [eyzwf, tpk]))])
### EXPERIMENT
constraints = [ExactlyKInARow(4, (psn, "ypkjl"))]
crossing = [smu, psn]
design=[ckt,smu,psn,tpk,eyzwf,erm,rrlxc]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
