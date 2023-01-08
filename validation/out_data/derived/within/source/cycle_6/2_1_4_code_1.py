from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vkv = Factor("vkv", ["our","teiznk","zti","ebiijo","wwu","dta","lreoe"])
def mnprc(vkv):
    return vkv == "lreoe"
def jns(vkv):
    return not (vkv == "lreoe")
uduxca = DerivedLevel("udho", WithinTrial(mnprc, [vkv]))
jajkvb = DerivedLevel("qlkb", WithinTrial(jns, [vkv]))
giq = Factor("azunp", [uduxca, jajkvb])

### EXPERIMENT
design=[vkv,giq]
crossing=[giq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END