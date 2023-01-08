from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eyejfk = Factor("eyejfk", ["btkg","oxf","rkxmwb","mzg","jjcq","wwk"])
def bcczje(eyejfk):
    return eyejfk != "jjcq"
def adogqt(eyejfk):
    return eyejfk == "jjcq"
bvcg = DerivedLevel("kuhms", WithinTrial(bcczje, [eyejfk]))
pmfsnn = DerivedLevel("zukl", WithinTrial(adogqt, [eyejfk]))
pxqq = Factor("htk", [bvcg, pmfsnn])

### EXPERIMENT
design=[eyejfk,pxqq]
crossing=[pxqq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END