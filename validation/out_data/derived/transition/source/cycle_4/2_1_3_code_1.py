from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jvd = Factor("jvd", ["qlov","feiuit","jsy","grr","eewt","ajb","ioroa"])
def mryd(jvd):
    return jvd[0] != "ajb" or jvd[-1] != "grr"
def vfynz(jvd):
    return not (jvd[0] != "ajb") and jvd[-1] == "grr"
yzrh = Factor("kxcewo", [DerivedLevel("occdnc", Transition(mryd, [jvd])), DerivedLevel("toqqq", Transition(vfynz, [jvd]))])
### EXPERIMENT
design=[jvd,yzrh]
crossing=[yzrh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END