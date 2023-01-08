from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eyejfk = Factor("eyejfk", ["btkg","oxf","rkxmwb","mzg","jjcq","wwk"])
def is_htk_kuhms(eyejfk):
    return eyejfk != "jjcq"
def is_htk_zukl(eyejfk):
    return not is_htk_kuhms(eyejfk)
htk= Factor("htk", [DerivedLevel("kuhms", WithinTrial(is_htk_kuhms, [eyejfk])), DerivedLevel("zukl", WithinTrial(is_htk_zukl, [eyejfk]))])

design=[eyejfk,htk]
crossing=[htk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END