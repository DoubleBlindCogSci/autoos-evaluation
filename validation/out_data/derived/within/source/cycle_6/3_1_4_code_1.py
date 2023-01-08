from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tiypz = Factor("tiypz", ["hsbkic","qrfj","dlo","sclcq","jut","qbm","dcsj","hsiqw"])
def gjmmjy(tiypz):
     return "hsiqw" == tiypz
def ofuxkj(tiypz):
     return tiypz == "qbm"
def celxs(tiypz):
     return (not gjmmjy(tiypz)) and (not tiypz == "qbm")
zxiq = DerivedLevel("idqcya", WithinTrial(gjmmjy, [tiypz]))
knnlqr = DerivedLevel("fqw", WithinTrial(ofuxkj, [tiypz]))
qay = DerivedLevel("jnt", WithinTrial(celxs, [tiypz]))
bqg = Factor("dsujjh", [zxiq, knnlqr, qay])

### EXPERIMENT
design=[tiypz,bqg]
crossing=[bqg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END