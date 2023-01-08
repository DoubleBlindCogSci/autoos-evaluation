from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vtn = Factor("vtn", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
ewjn = Factor("ewjn", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
bvind = Factor("bvind", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
def is_jjev_pbx(vtn, ewjn, bvind):
    return vtn == ewjn
def is_jjev_dmhmm(vtn, ewjn, bvind):
    return vtn != ewjn and bvind == vtn
def is_jjev_xegnon(vtn, ewjn, bvind):
    return vtn != ewjn and bvind != vtn
jjev = Factor("jjev", [DerivedLevel("pbx", WithinTrial(is_jjev_pbx, [vtn, ewjn, bvind])), DerivedLevel("dmhmm", WithinTrial(is_jjev_dmhmm, [vtn, ewjn, bvind])), DerivedLevel("xegnon", WithinTrial(is_jjev_xegnon, [vtn, ewjn, bvind]))])

design=[vtn,ewjn,bvind,jjev]
crossing=[jjev]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END