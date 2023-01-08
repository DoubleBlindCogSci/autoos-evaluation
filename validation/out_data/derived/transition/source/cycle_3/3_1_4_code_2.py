from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nwk = Factor("nwk", ["fvnll","joayyf","hump","img","muti","pncppn","fwkjs","vkfvf"])
def is_twha_boqyr(nwk):
    return nwk[-1] == "hump" and nwk[0] != "pncppn"
def is_twha_xfme(nwk):
    return nwk[-1] != "hump" and nwk[0] == "pncppn"
def is_twha_ppjfl(nwk):
    return not (is_twha_boqyr(nwk) or is_twha_xfme(nwk))
twha= Factor("twha", [DerivedLevel("boqyr", Transition(is_twha_boqyr, [nwk])), DerivedLevel("xfme", Transition(is_twha_xfme, [nwk])), DerivedLevel("ppjfl", Transition(is_twha_ppjfl, [nwk]))])

design=[nwk,twha]
crossing=[twha]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
