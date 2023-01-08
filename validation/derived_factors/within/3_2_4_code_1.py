from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
voy = Factor("voy", ["vcl","wfp","jrhhib","xgzu","svmyom","kuezq","vdk"])
znaqm = Factor("znaqm", ["vcl","wfp","jrhhib","xgzu","svmyom","kuezq","vdk"])
cfyys = Factor("cfyys", ["vcl","wfp","jrhhib","xgzu","svmyom","kuezq","vdk"])
def vdzez(voy, cfyys, znaqm):
     return cfyys == voy
def opexkb(voy, cfyys, znaqm):
     return cfyys != voy and voy == znaqm
def qfsext(voy, cfyys, znaqm):
     return (not vdzez(voy, cfyys, znaqm)) and (not voy == znaqm)
zlfvvt = Factor("ckzpq", [DerivedLevel("xjx", WithinTrial(vdzez, [voy, znaqm, cfyys])), DerivedLevel("eztha", WithinTrial(opexkb, [voy, znaqm, cfyys])),DerivedLevel("mkjja", WithinTrial(qfsext, [voy, znaqm, cfyys]))])
### EXPERIMENT
design=[voy,znaqm,cfyys,zlfvvt]
crossing=[zlfvvt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END