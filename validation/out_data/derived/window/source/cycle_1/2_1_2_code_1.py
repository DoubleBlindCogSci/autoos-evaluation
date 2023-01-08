from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qasz = Factor("qasz", ["optefg","usdn","pdehkm","eiyzf","jyxdrm","hoq"])
def dwm(qasz):
    return qasz[-2] != "jyxdrm" and qasz[-3] != "optefg"
def ucdtp(qasz):
    return qasz[-2] == "jyxdrm" or not (qasz[-3] != "optefg")
emkon = DerivedLevel("mzrq", Window(dwm, [qasz],4,1))
mcygv = DerivedLevel("bfurc", Window(ucdtp, [qasz],4,1))
aewe = Factor("uix", [emkon, mcygv])

### EXPERIMENT
design=[qasz,aewe]
crossing=[aewe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END