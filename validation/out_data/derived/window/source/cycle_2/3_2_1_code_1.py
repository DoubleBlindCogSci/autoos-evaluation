from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eqhxp = Factor("eqhxp", ["oaylp","uisvq","mvc","trrtn","etz","vvixp"])
fkxb = Factor("fkxb", ["zqthl","eoxhfp","nipkq","fvud","sxndfe","teif","lzeks","brcsus"])
def umiy(eqhxp, fkxb):
     return "etz" == eqhxp[0] and fkxb[-1] != "teif"
def ptui(eqhxp, fkxb):
     return "etz" != eqhxp[0] and  fkxb[-1] == "teif"
def kvvy(eqhxp, fkxb):
     return (eqhxp[0] != "etz") and (fkxb[-1] != "teif")
lzoz = DerivedLevel("tmu", Window(umiy, [eqhxp, fkxb],2,1))
shykef = DerivedLevel("qdhzdb", Window(ptui, [eqhxp, fkxb],2,1))
hyrw = DerivedLevel("qkejh", Window(kvvy, [eqhxp, fkxb],2,1))
pvbnd = Factor("url", [lzoz, shykef, hyrw])

### EXPERIMENT
design=[eqhxp,fkxb,pvbnd]
crossing=[pvbnd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END