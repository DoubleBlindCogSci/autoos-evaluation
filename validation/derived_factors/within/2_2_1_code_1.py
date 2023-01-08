from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iklr = Factor("iklr", ["nonej","rdo","dno","puazmx","phbtw","amcgw"])
xtk = Factor("xtk", ["nonej","rdo","dno","puazmx","phbtw","amcgw"])
ihzzvs = Factor("ihzzvs", ["nonej","rdo","dno","puazmx","phbtw","amcgw"])
def mhw(iklr, xtk, ihzzvs):
    return iklr == xtk
def kifgw(iklr, xtk, ihzzvs):
    return iklr != xtk
ezv = Factor("ocyikz", [DerivedLevel("jaxwg", WithinTrial(mhw, [iklr, xtk, ihzzvs])), DerivedLevel("wmduny", WithinTrial(kifgw, [iklr, xtk, ihzzvs]))])
### EXPERIMENT
design=[iklr,xtk,ihzzvs,ezv]
crossing=[ezv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END