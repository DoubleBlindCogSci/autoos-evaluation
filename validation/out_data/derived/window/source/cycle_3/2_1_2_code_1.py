from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ybxlxi = Factor("ybxlxi", ["tvzo","zlobz","kauhfp","vazzo","qlwxy","nxhhsi"])
def hcochr(ybxlxi):
    return ybxlxi[-2] == "zlobz" or ybxlxi[-3] == "kauhfp"
def otxjdy(ybxlxi):
    return not hcochr(ybxlxi)
omenah = DerivedLevel("jlkvr", Window(hcochr, [ybxlxi],4,1))
qvxof = DerivedLevel("hlpzh", Window(otxjdy, [ybxlxi],4,1))
bkhj = Factor("byjy", [omenah, qvxof])

### EXPERIMENT
design=[ybxlxi,bkhj]
crossing=[bkhj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END