from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tiypz = Factor("tiypz", ["hsbkic","qrfj","dlo","sclcq","jut","qbm","dcsj","hsiqw"])
def is_dsujjh_idqcya(tiypz):
    return tiypz == "hsiqw"
def is_dsujjh_fqw(tiypz):
    return tiypz == "qbm"
def is_dsujjh_jnt(tiypz):
    return not (is_dsujjh_idqcya(tiypz) or is_dsujjh_fqw(tiypz))
dsujjh = Factor("dsujjh", [DerivedLevel("idqcya", WithinTrial(is_dsujjh_idqcya, [tiypz])), DerivedLevel("fqw", WithinTrial(is_dsujjh_fqw, [tiypz])), DerivedLevel("jnt", WithinTrial(is_dsujjh_jnt, [tiypz]))])

design=[tiypz,dsujjh]
crossing=[dsujjh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END