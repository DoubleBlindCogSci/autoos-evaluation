from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wgy = Factor("wgy", ["kexsa","ojvw","rjs","yhcave","odywkz","yqwqrq"])
def ymrt(wgy):
    return wgy[-3] == "kexsa" and wgy[-1] != "yqwqrq"
def yomv(wgy):
    return not ymrt(wgy)
ricf = Factor("cixq", [DerivedLevel("mqes", Window(ymrt, [wgy],4,1)), DerivedLevel("fexbma", Window(yomv, [wgy],4,1))])
### EXPERIMENT
design=[wgy,ricf]
crossing=[ricf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END