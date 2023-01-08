from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qbr = Factor("qbr", ["oze","wuxugm","whq","guj","uqicr","mycich","juuhx","axhc"])
lpnhi = Factor("lpnhi", ["iwrg","nkk","upqzq","iyeis","lslmc","kpl","hmhisr","yfqa"])
def uednih(qbr, lpnhi):
     return qbr[0] == "oze" and lpnhi[-1] != "hmhisr"
def apzwj(qbr, lpnhi):
     return "oze" != qbr[0] and  lpnhi[-1] == "hmhisr"
def arawt(qbr, lpnhi):
     return (not uednih(qbr, lpnhi)) and (not apzwj(qbr, lpnhi))
csugv = DerivedLevel("kdby", Window(uednih, [qbr, lpnhi],2,1))
klszcv = DerivedLevel("ucb", Window(apzwj, [qbr, lpnhi],2,1))
qyyr = DerivedLevel("tnqpc", Window(arawt, [qbr, lpnhi],2,1))
xvhmxl = Factor("odsxra", [csugv, klszcv, qyyr])

### EXPERIMENT
design=[qbr,lpnhi,xvhmxl]
crossing=[xvhmxl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END