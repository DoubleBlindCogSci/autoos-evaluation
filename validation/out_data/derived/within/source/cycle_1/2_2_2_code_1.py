from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dkqkm = Factor("dkqkm", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
jmai = Factor("jmai", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
qtb = Factor("qtb", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
def ukpjvo(dkqkm, qtb, jmai):
    return dkqkm != qtb or dkqkm == jmai
def aphfj(dkqkm, qtb, jmai):
    return not (dkqkm != qtb) and dkqkm != jmai
hiv = DerivedLevel("rvgss", WithinTrial(ukpjvo, [dkqkm, jmai, qtb]))
wbdl = DerivedLevel("qdrcjx", WithinTrial(aphfj, [dkqkm, jmai, qtb]))
ehi = Factor("corru", [hiv, wbdl])

### EXPERIMENT
design=[dkqkm,jmai,qtb,ehi]
crossing=[ehi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END