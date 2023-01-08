from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cbjmq = Factor("cbjmq", ["epukqk","yod","sho","wfdwa","cxq","zdm"])
xtm = Factor("xtm", ["hqh","piswjo","aqa","zsp","bawpi","cshg"])
def ydgwbz(cbjmq, xtm):
    return cbjmq[-2] != "sho" or xtm[0] != "cshg"
def ouo(cbjmq,xtm):
    return not (cbjmq[-2] != "sho") and xtm[0] == "cshg"
suy = DerivedLevel("lzwjda", Window(ydgwbz, [cbjmq, xtm],3,1))
zfy = DerivedLevel("wkx", Window(ouo, [cbjmq, xtm],3,1))
fgcfo = Factor("iljb", [suy, zfy])

### EXPERIMENT
design=[cbjmq,xtm,fgcfo]
crossing=[fgcfo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END