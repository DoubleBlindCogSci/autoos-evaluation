from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xczrq = Factor("xczrq", ["doby","xtplr","zfv","echghq","esnx","xhfanc","hune"])
def kkzwc(xczrq):
    return xczrq != "zfv"
def glfw(xczrq):
    return not kkzwc(xczrq)
rya = DerivedLevel("njy", WithinTrial(kkzwc, [xczrq]))
gln = DerivedLevel("bqgh", WithinTrial(glfw, [xczrq]))
syzk = Factor("rmg", [rya, gln])

### EXPERIMENT
design=[xczrq,syzk]
crossing=[syzk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END