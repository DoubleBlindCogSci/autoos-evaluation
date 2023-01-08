from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eapq = Factor("eapq", ["vhnpdu","pbatp","lgksu","adm","lzk","xaxtof","hrtrsx"])
def is_xdgdqc_bidy(eapq):
    return eapq[-2] == "adm" and eapq[-1] != "adm"
def is_xdgdqc_qzjjv(eapq):
    return eapq[-2] != "adm" and eapq[-1] == "hrtrsx"
def is_xdgdqc_wpjoz(eapq):
    return not (is_xdgdqc_bidy(eapq) or is_xdgdqc_qzjjv(eapq))
xdgdqc = Factor("xdgdqc", [DerivedLevel("bidy", Window(is_xdgdqc_bidy, [eapq], 3, 1)), DerivedLevel("qzjjv", Window(is_xdgdqc_qzjjv, [eapq], 3, 1)), DerivedLevel("wpjoz", Window(is_xdgdqc_wpjoz, [eapq], 3, 1))])

design=[eapq,xdgdqc]
crossing=[xdgdqc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END