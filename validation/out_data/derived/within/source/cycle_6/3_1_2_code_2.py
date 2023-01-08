from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vilah = Factor("vilah", ["gih","smc","rdfv","kto","nvv","shzkx","mpplx","fdd"])
def is_lvbj_gkd(vilah):
    return vilah == "nvv"
def is_lvbj_ohs(vilah):
    return vilah == "smc"
def is_lvbj_vgsu(vilah):
    return not (is_lvbj_gkd(vilah) or is_lvbj_ohs(vilah))
lvbj = Factor("lvbj", [DerivedLevel("gkd", WithinTrial(is_lvbj_gkd, [vilah])), DerivedLevel("ohs", WithinTrial(is_lvbj_ohs, [vilah])), DerivedLevel("vgsu", WithinTrial(is_lvbj_vgsu, [vilah]))])

design=[vilah,lvbj]
crossing=[lvbj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END