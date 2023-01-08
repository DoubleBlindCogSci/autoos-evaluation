from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dkqkm= Factor("dkqkm", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
jmai= Factor("jmai", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])
qtb= Factor("qtb", ["aluuw","pee","imfilh","tnej","xocj","bgskn"])

def is_corru_rvgss(dkqkm, jmai, qtb):
    return dkqkm != qtb or dkqkm == jmai
def is_corru_qdrcjx(dkqkm, jmai, qtb):
    return dkqkm == qtb and dkqkm != jmai
corru= Factor("corru", [DerivedLevel("rvgss", WithinTrial(is_corru_rvgss, [dkqkm, jmai, qtb])), DerivedLevel("qdrcjx", WithinTrial(is_corru_qdrcjx, [dkqkm, jmai, qtb]))])


design=[dkqkm,jmai,qtb,corru]
crossing=[corru]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
