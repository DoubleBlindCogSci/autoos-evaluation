from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ago = Factor("ago", ["bbbn","dlucvg","xjya","lgu","ezfgig","fhtx","zhcm"])
def is_fsgf_pjd(ago):
    return ago[-1] == "bbbn" and ago[0] != "bbbn"
def is_fsgf_hjqc(ago):
    return ago[-1] != "bbbn" and ago[0] == "fhtx"
def is_fsgf_kqaxgo(ago):
    return not (is_fsgf_pjd(ago) or is_fsgf_hjqc(ago))
fsgf = Factor("fsgf", [DerivedLevel("pjd", Window(is_fsgf_pjd, [ago], 2, 1)), DerivedLevel("hjqc", Window(is_fsgf_hjqc, [ago], 2, 1)), DerivedLevel("kqaxgo", Window(is_fsgf_kqaxgo, [ago], 2, 1))])

design=[ago,fsgf]
crossing=[fsgf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END