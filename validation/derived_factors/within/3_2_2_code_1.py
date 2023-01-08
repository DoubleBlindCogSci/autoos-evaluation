from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cjvn = Factor("cjvn", ["wysk","rqwpcs","jip","znmw","qzd","qnxon","luadp","pzlnoo"])
vhvm = Factor("vhvm", ["mll","uqshnl","syoqcq","zgxlr","gzrkh","wuuycd","xwx"])
def aci(cjvn, vhvm):
     return cjvn == "rqwpcs"
def cydha(cjvn, vhvm):
     return "rqwpcs" != cjvn and  vhvm == "syoqcq"
def tzejv(cjvn, vhvm):
     return (not aci(cjvn, vhvm)) and (not cydha(cjvn, vhvm))
pfqyn = DerivedLevel("kwpf", WithinTrial(aci, [cjvn, vhvm]))
vilmk = DerivedLevel("kyrs", WithinTrial(cydha, [cjvn, vhvm]))
qxhyw = DerivedLevel("ybmuj", WithinTrial(tzejv, [cjvn, vhvm]))
kdzcea = Factor("uogby", [pfqyn, vilmk, qxhyw])

### EXPERIMENT
design=[cjvn,vhvm,kdzcea]
crossing=[kdzcea]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END