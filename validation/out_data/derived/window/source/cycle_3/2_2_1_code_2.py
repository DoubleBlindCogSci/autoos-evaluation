from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
crzz = Factor("crzz", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
svrko = Factor("svrko", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
yurqow = Factor("yurqow", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
def is_vqh_hmks(crzz, svrko, yurqow):
    return crzz[-3] != yurqow[-2] and crzz[-2] != svrko[-3]
def is_vqh_aqjgfj(crzz, svrko, yurqow):
    return not is_vqh_hmks(crzz, svrko, yurqow)
vqh= Factor("vqh", [DerivedLevel("hmks", Window(is_vqh_hmks, [crzz, svrko, yurqow], 4, 1)), DerivedLevel("aqjgfj", Window(is_vqh_aqjgfj, [crzz, svrko, yurqow], 4, 1))])

design=[crzz,svrko,yurqow,vqh]
crossing=[vqh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
