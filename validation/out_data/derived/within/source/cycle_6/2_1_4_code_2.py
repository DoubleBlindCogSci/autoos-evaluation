from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vkv = Factor("vkv", ["our","teiznk","zti","ebiijo","wwu","dta","lreoe"])
def is_azunp_udho(vkv):
    return vkv == "lreoe"
def is_azunp_qlkb(vkv):
    return not is_azunp_udho(vkv)
azunp = Factor("azunp", [DerivedLevel("udho", WithinTrial(is_azunp_udho, [vkv])), DerivedLevel("qlkb", WithinTrial(is_azunp_qlkb, [vkv]))])

design=[vkv,azunp]
crossing=[azunp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END