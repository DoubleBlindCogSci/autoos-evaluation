from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xkj = Factor("xkj", ["ljiv","hitf","jctbq","savcm","gyed","cdrgmp","xynbu","anvp"])
def is_lssd_jshn(xkj):
    return xkj == "savcm"
def is_lssd_ztvy(xkj):
    return xkj == "cdrgmp"
def is_lssd_enxao(xkj):
    return not (is_lssd_jshn(xkj) or is_lssd_ztvy(xkj))
lssd = Factor("lssd", [DerivedLevel("jshn", WithinTrial(is_lssd_jshn, [xkj])), DerivedLevel("ztvy", WithinTrial(is_lssd_ztvy, [xkj])), DerivedLevel("enxao", WithinTrial(is_lssd_enxao, [xkj]))])

design=[xkj,lssd]
crossing=[lssd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END