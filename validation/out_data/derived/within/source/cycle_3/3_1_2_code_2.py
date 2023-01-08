from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qbzh = Factor("qbzh", ["ginswl","sxl","kxzb","xbq","dibh","lyz"])
def is_boymv_emqd(qbzh):
    return qbzh == "dibh"
def is_boymv_kmrzf(qbzh):
    return qbzh == "lyz"
def is_boymv_jxeygo(qbzh):
    return not (is_boymv_emqd(qbzh) or is_boymv_kmrzf(qbzh))
boymv= Factor("boymv", [DerivedLevel("emqd", WithinTrial(is_boymv_emqd, [qbzh])), DerivedLevel("kmrzf", WithinTrial(is_boymv_kmrzf, [qbzh])), DerivedLevel("jxeygo", WithinTrial(is_boymv_jxeygo, [qbzh]))])

design=[qbzh,boymv]
crossing=[boymv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
