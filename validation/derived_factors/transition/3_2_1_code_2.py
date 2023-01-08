from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hruxe = Factor("hruxe", ["ejbn","vblag","ksrq","epttpg","uyp","mooj","zwqnb","yojs"])
whb = Factor("whb", ["bxz","wwmca","ixvf","wod","dzxlz","rwip","kmf","bpt"])
def is_ftubtu_mzyagu(hruxe, whb):
    return hruxe[-1] == "ejbn" and whb[0] != "ixvf"
def is_ftubtu_mlgu(hruxe, whb):
    return hruxe[-1] != "ejbn" and whb[0] == "ixvf"
def is_ftubtu_glezlm(hruxe, whb):
    return not (is_ftubtu_mzyagu(hruxe, whb) or is_ftubtu_mlgu(hruxe, whb))
ftubtu = Factor("ftubtu", [DerivedLevel("mzyagu", Transition(is_ftubtu_mzyagu, [hruxe, whb])), DerivedLevel("mlgu", Transition(is_ftubtu_mlgu, [hruxe, whb])), DerivedLevel("glezlm", Transition(is_ftubtu_glezlm, [hruxe, whb]))])

design=[hruxe,whb,ftubtu]
crossing=[ftubtu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END