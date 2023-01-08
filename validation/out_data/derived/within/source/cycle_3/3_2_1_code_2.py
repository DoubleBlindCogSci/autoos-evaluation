from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ykmc = Factor("ykmc", ["vyle","yuvder","xxf","loup","hyh","fjptm","cgrl"])
okg = Factor("okg", ["lthe","oeru","pjzss","xtdg","mvmk","afop","pxg"])
def is_ncv_pxocro(ykmc, okg):
    return ykmc == "cgrl"
def is_ncv_xoqhut(ykmc, okg):
    return ykmc != "cgrl" and okg == "lthe"
def is_ncv_jgz(ykmc, okg):
    return not (is_ncv_pxocro(ykmc, okg) or is_ncv_xoqhut(ykmc, okg))
ncv= Factor("ncv", [DerivedLevel("pxocro", WithinTrial(is_ncv_pxocro, [ykmc, okg])), DerivedLevel("xoqhut", WithinTrial(is_ncv_xoqhut, [ykmc, okg])), DerivedLevel("jgz", WithinTrial(is_ncv_jgz, [ykmc, okg]))])

design=[ykmc,okg,ncv]
crossing=[ncv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
