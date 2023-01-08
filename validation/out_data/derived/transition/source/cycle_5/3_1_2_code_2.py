from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gux = Factor("gux", ["mqb","bimndj","gwta","mgd","fttjig","fwe","hhn","juqlf"])
def is_uakm_prbuti(gux):
    return gux[-1] == "fwe" and gux[0] != "gwta"
def is_uakm_gstiro(gux):
    return gux[-1] != "fwe" and gux[0] == "gwta"
def is_uakm_wjb(gux):
    return not (is_uakm_prbuti(gux) or is_uakm_gstiro(gux))
uakm = Factor("uakm", [DerivedLevel("prbuti", Transition(is_uakm_prbuti, [gux])), DerivedLevel("gstiro", Transition(is_uakm_gstiro, [gux])), DerivedLevel("wjb", Transition(is_uakm_wjb, [gux]))])

design=[gux,uakm]
crossing=[uakm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END