from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ceu = Factor("ceu", ["rpcrs","udkb","twmaox","qaae","nvexxh","ncjnk","chnb"])
bdyt = Factor("bdyt", ["lqion","yineba","ycdloc","wshkm","sxaltc"])
def is_jep_ekkemy(ceu, bdyt):
    return ceu[-1] == "rpcrs" and bdyt[-3] == "lqion"
def is_jep_koffu(ceu, bdyt):
    return not is_jep_ekkemy(ceu, bdyt)
jep= Factor("jep", [DerivedLevel("ekkemy", Window(is_jep_ekkemy, [ceu, bdyt], 4, 1)), DerivedLevel("koffu", Window(is_jep_koffu, [ceu, bdyt], 4, 1))])

design=[ceu,bdyt,jep]
crossing=[jep]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
