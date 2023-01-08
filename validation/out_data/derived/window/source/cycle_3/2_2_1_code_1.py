from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
crzz = Factor("crzz", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
svrko = Factor("svrko", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
yurqow = Factor("yurqow", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
def vmykz(crzz, yurqow, svrko):
    return crzz[-3] != yurqow[-2] and crzz[-2] != svrko[-3]
def vctfq(crzz, yurqow, svrko):
    return not (crzz[-3] != yurqow[-2]) or crzz[-2] == svrko[-3]
juqg = Factor("vqh", [DerivedLevel("hmks", Window(vmykz, [crzz, svrko, yurqow],4,1)), DerivedLevel("aqjgfj", Window(vctfq, [crzz, svrko, yurqow],4,1))])
### EXPERIMENT
design=[crzz,svrko,yurqow,juqg]
crossing=[juqg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END