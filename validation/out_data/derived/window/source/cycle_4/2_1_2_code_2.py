from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wgy = Factor("wgy", ["kexsa","ojvw","rjs","yhcave","odywkz","yqwqrq"])
def is_cixq_mqes(wgy):
    return wgy[-3] == "kexsa" and wgy[-1] != "yqwqrq"
def is_cixq_fexbma(wgy):
    return not is_cixq_mqes(wgy)
cixq= Factor("cixq", [DerivedLevel("mqes", Window(is_cixq_mqes, [wgy], 4, 1)), DerivedLevel("fexbma", Window(is_cixq_fexbma, [wgy], 4, 1))])

design=[wgy,cixq]
crossing=[cixq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END