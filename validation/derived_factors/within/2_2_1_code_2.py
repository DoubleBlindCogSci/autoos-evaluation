from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iklr = Factor("iklr", ["nonej","rdo","dno","puazmx","phbtw","amcgw"])
xtk = Factor("xtk", ["nonej","rdo","dno","puazmx","phbtw","amcgw"])
ihzzvs = Factor("ihzzvs", ["nonej","rdo","dno","puazmx","phbtw","amcgw"])
def is_ocyikz_jaxwg(iklr, xtk, ihzzvs):
    return iklr == xtk
def is_ocyikz_wmduny(iklr, xtk, ihzzvs):
    return not is_ocyikz_jaxwg(iklr, xtk, ihzzvs)
ocyikz = Factor("ocyikz", [DerivedLevel("jaxwg", WithinTrial(is_ocyikz_jaxwg, [iklr, xtk, ihzzvs])), DerivedLevel("wmduny", WithinTrial(is_ocyikz_wmduny, [iklr, xtk, ihzzvs]))])

design=[iklr,xtk,ihzzvs,ocyikz]
crossing=[ocyikz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END