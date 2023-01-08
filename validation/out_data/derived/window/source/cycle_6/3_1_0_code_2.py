from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ensgf = Factor("ensgf", ["uhk","vjri","vln","zrw","mbemo","rmnz"])
def is_qwkebc_gynbxm(ensgf):
    return ensgf[-2] == "vln" and ensgf[-1] != "vln"
def is_qwkebc_bknfk(ensgf):
    return ensgf[-2] != "vln" and ensgf[-1] == "mbemo"
def is_qwkebc_nqatc(ensgf):
    return not (is_qwkebc_gynbxm(ensgf) or is_qwkebc_bknfk(ensgf))
qwkebc = Factor("qwkebc", [DerivedLevel("gynbxm", Window(is_qwkebc_gynbxm, [ensgf], 3, 1)), DerivedLevel("bknfk", Window(is_qwkebc_bknfk, [ensgf], 3, 1)), DerivedLevel("nqatc", Window(is_qwkebc_nqatc, [ensgf], 3, 1))])

design=[ensgf,qwkebc]
crossing=[qwkebc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END