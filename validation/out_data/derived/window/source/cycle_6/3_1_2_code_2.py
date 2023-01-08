from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ptqz = Factor("ptqz", ["ris","hkeewa","htq","hqizy","zya","qudqay","bigo","ftgj"])
def is_vge_dkhvb(ptqz):
    return ptqz[0] == "hqizy" and ptqz[-1] != "hqizy"
def is_vge_xhb(ptqz):
    return ptqz[0] != "hqizy" and ptqz[-1] == "qudqay"
def is_vge_wvdtqo(ptqz):
    return not (is_vge_dkhvb(ptqz) or is_vge_xhb(ptqz))
vge = Factor("vge", [DerivedLevel("dkhvb", Window(is_vge_dkhvb, [ptqz], 2, 1)), DerivedLevel("xhb", Window(is_vge_xhb, [ptqz], 2, 1)), DerivedLevel("wvdtqo", Window(is_vge_wvdtqo, [ptqz], 2, 1))])

design=[ptqz,vge]
crossing=[vge]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END