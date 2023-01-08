from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rqs = Factor("rqs", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
kcxu = Factor("kcxu", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
ouebx = Factor("ouebx", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
def is_smd_lzdlm(rqs, kcxu, ouebx):
    return ouebx == rqs
def is_smd_kyvmnu(rqs, kcxu, ouebx):
    return ouebx != rqs and kcxu == rqs
def is_smd_qddvj(rqs, kcxu, ouebx):
    return ouebx != rqs and kcxu != rqs
smd= Factor("smd", [DerivedLevel("lzdlm", WithinTrial(is_smd_lzdlm, [rqs, kcxu, ouebx])), DerivedLevel("kyvmnu", WithinTrial(is_smd_kyvmnu, [rqs, kcxu, ouebx])), DerivedLevel("qddvj", WithinTrial(is_smd_qddvj, [rqs, kcxu, ouebx]))])

design=[rqs,kcxu,ouebx,smd]
crossing=[smd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END