from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ffp = Factor("ffp", ["fmie","buekwg","cybl","evsdjz","inxtj","rbc"])
def is_pug_ydoqi(ffp):
    return ffp[-2] == "rbc" and ffp[-1] != "rbc"
def is_pug_qsap(ffp):
    return ffp[-2] != "rbc" and ffp[-1] == "buekwg"
def is_pug_vgta(ffp):
    return not (is_pug_ydoqi(ffp) or is_pug_qsap(ffp))
pug = Factor("pug", [DerivedLevel("ydoqi", Window(is_pug_ydoqi, [ffp], 3, 1)), DerivedLevel("qsap", Window(is_pug_qsap, [ffp], 3, 1)), DerivedLevel("vgta", Window(is_pug_vgta, [ffp], 3, 1))])

design=[ffp,pug]
crossing=[pug]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END