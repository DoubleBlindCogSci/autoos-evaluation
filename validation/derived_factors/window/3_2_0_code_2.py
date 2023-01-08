from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qbr = Factor("qbr", ["oze","wuxugm","whq","guj","uqicr","mycich","juuhx","axhc"])
lpnhi = Factor("lpnhi", ["iwrg","nkk","upqzq","iyeis","lslmc","kpl","hmhisr","yfqa"])
def is_odsxra_kdby(qbr, lpnhi):
    return qbr[0] == "oze" and lpnhi[-1] != "hmhisr"
def is_odsxra_ucb(qbr, lpnhi):
    return qbr[0] != "oze" and lpnhi[-1] == "hmhisr"
def is_odsxra_tnqpc(qbr, lpnhi):
    return not (is_odsxra_kdby(qbr, lpnhi) or is_odsxra_ucb(qbr, lpnhi))
odsxra = Factor("odsxra", [DerivedLevel("kdby", Window(is_odsxra_kdby, [qbr, lpnhi], 2, 1)), DerivedLevel("ucb", Window(is_odsxra_ucb, [qbr, lpnhi], 2, 1)), DerivedLevel("tnqpc", Window(is_odsxra_tnqpc, [qbr, lpnhi], 2, 1))])

design=[qbr,lpnhi,odsxra]
crossing=[odsxra]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END