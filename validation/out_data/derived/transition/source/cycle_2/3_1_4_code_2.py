from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rwkex= Factor("rwkex", ["ievjo","oaostz","uxhbc","hlyauw","lis","otcr"])
def is_klc_ufpf(rwkex):
    return rwkex[0] == "hlyauw" and rwkex[-1] != "lis"
def is_klc_lrbn(rwkex):
    return rwkex[0] != "hlyauw" and rwkex[-1] == "lis"
def is_klc_mwop(rwkex):
    return not (is_klc_ufpf(rwkex) or is_klc_lrbn(rwkex))
klc= Factor("klc", [DerivedLevel("ufpf", Transition(is_klc_ufpf, [rwkex])), DerivedLevel("lrbn", Transition(is_klc_lrbn, [rwkex])), DerivedLevel("mwop", Transition(is_klc_mwop, [rwkex]))])

design=[rwkex,klc]
crossing=[klc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
