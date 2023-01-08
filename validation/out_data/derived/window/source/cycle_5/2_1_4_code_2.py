from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jlb = Factor("jlb", ["gyy","aklr","vsgh","vmokyj","rwhz","husnen"])
def is_cyt_jklom(jlb):
    return jlb[-1] != "vmokyj" or jlb[0] == "aklr"
def is_cyt_kkkge(jlb):
    return not is_cyt_jklom(jlb)
cyt = Factor("cyt", [DerivedLevel("jklom", Window(is_cyt_jklom, [jlb], 2, 1)), DerivedLevel("kkkge", Window(is_cyt_kkkge, [jlb], 2, 1))])

design=[jlb,cyt]
crossing=[cyt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END