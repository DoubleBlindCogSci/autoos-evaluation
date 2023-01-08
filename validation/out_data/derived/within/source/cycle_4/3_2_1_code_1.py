from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rqs = Factor("rqs", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
kcxu = Factor("kcxu", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
ouebx = Factor("ouebx", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
def tuwln(rqs, ouebx, kcxu):
     return ouebx == rqs
def pxf(rqs, ouebx, kcxu):
     return ouebx != rqs and kcxu == rqs
def bixv(rqs, ouebx, kcxu):
     return (rqs != ouebx) and (rqs != kcxu)
abde = DerivedLevel("lzdlm", WithinTrial(tuwln, [rqs, kcxu, ouebx]))
nbr = DerivedLevel("kyvmnu", WithinTrial(pxf, [rqs, kcxu, ouebx]))
llem = DerivedLevel("qddvj", WithinTrial(bixv, [rqs, kcxu, ouebx]))
fsn = Factor("smd", [abde, nbr, llem])

### EXPERIMENT
design=[rqs,kcxu,ouebx,fsn]
crossing=[fsn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END