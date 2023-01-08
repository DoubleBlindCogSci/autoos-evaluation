from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qwiy= Factor("qwiy", ["dgu","qvgr","yzrvv","gjiu","czhpzo","fthdvo"])
rnrlm= Factor("rnrlm", ["slu","icpjh","ihfoa","kszigq","vgrk","ehej","eqm","lyovq"])
def is_koxrmj_yqcwc(qwiy, rnrlm):
    return qwiy == "dgu"
def is_koxrmj_gscts(qwiy, rnrlm):
    return qwiy != "dgu" and rnrlm == "lyovq"
def is_koxrmj_eqh(qwiy, rnrlm):
    return qwiy != "dgu" and rnrlm != "lyovq"
koxrmj= Factor("koxrmj", [DerivedLevel("yqcwc", WithinTrial(is_koxrmj_yqcwc, [qwiy, rnrlm])), DerivedLevel("gscts", WithinTrial(is_koxrmj_gscts, [qwiy, rnrlm])), DerivedLevel("eqh", WithinTrial(is_koxrmj_eqh, [qwiy, rnrlm]))])

design=[qwiy,rnrlm, koxrmj]
crossing=[koxrmj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
