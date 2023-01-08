from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qwiy = Factor("qwiy", ["dgu","qvgr","yzrvv","gjiu","czhpzo","fthdvo"])
rnrlm = Factor("rnrlm", ["slu","icpjh","ihfoa","kszigq","vgrk","ehej","eqm","lyovq"])
def kseuvv(qwiy, rnrlm):
     return qwiy == "dgu"
def weh(qwiy, rnrlm):
     return "dgu" != qwiy and  rnrlm == "lyovq"
def tbvd(qwiy, rnrlm):
     return (not kseuvv(qwiy, rnrlm)) and (rnrlm != "lyovq")
mphwlt = DerivedLevel("yqcwc", WithinTrial(kseuvv, [qwiy, rnrlm]))
bvuk = DerivedLevel("gscts", WithinTrial(weh, [qwiy, rnrlm]))
tzdpiz = DerivedLevel("eqh", WithinTrial(tbvd, [qwiy, rnrlm]))
gani = Factor("koxrmj", [mphwlt, bvuk, tzdpiz])

### EXPERIMENT
design=[qwiy,rnrlm,gani]
crossing=[gani]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END