from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ceu = Factor("ceu", ["rpcrs","udkb","twmaox","qaae","nvexxh","ncjnk","chnb"])
bdyt = Factor("bdyt", ["lqion","yineba","ycdloc","wshkm","sxaltc"])
def syp(ceu, bdyt):
    return ceu[-1] == "rpcrs" and bdyt[-3] == "lqion"
def cay(ceu,bdyt):
    return ceu[-1] != "rpcrs" or not (bdyt[-3] == "lqion")
kaxu = Factor("jep", [DerivedLevel("ekkemy", Window(syp, [ceu, bdyt],4,1)), DerivedLevel("koffu", Window(cay, [ceu, bdyt],4,1))])
### EXPERIMENT
design=[ceu,bdyt,kaxu]
crossing=[kaxu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END