from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cbjmq = Factor("cbjmq", ["epukqk","yod","sho","wfdwa","cxq","zdm"])
xtm = Factor("xtm", ["hqh","piswjo","aqa","zsp","bawpi","cshg"])
def is_iljb_lzwjda(cbjmq, xtm):
    return cbjmq[-2] != "sho" or xtm[0] != "cshg"
def is_iljb_wkx(cbjmq, xtm):
    return not is_iljb_lzwjda(cbjmq, xtm)
iljb = Factor("iljb", [DerivedLevel("lzwjda", Window(is_iljb_lzwjda, [cbjmq, xtm], 3, 1)), DerivedLevel("wkx", Window(is_iljb_wkx, [cbjmq, xtm], 3, 1))])

design=[cbjmq,xtm,iljb]
crossing=[iljb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END