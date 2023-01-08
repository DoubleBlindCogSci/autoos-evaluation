from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wov = Factor("wov", ["lgit","wxcyas","zle","rlse","kum","zkgbw"])
def is_kuuz_kgwv(wov):
    return wov[-1] == "lgit" and wov[0] != "wxcyas"
def is_kuuz_jxl(wov):
    return wov[-1] != "lgit" and wov[0] == "wxcyas"
def is_kuuz_sfam(wov):
    return not (is_kuuz_kgwv(wov) or is_kuuz_jxl(wov))
kuuz = Factor("kuuz", [DerivedLevel("kgwv", Transition(is_kuuz_kgwv, [wov])), DerivedLevel("jxl", Transition(is_kuuz_jxl, [wov])), DerivedLevel("sfam", Transition(is_kuuz_sfam, [wov]))])

design=[wov,kuuz]
crossing=[kuuz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END