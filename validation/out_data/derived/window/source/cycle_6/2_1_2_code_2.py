from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
faocwk = Factor("faocwk", ["ckgmnr","tvl","gtqoo","vwx","hjdt","hqv"])
def is_eargi_xmehrd(faocwk):
    return faocwk[0] != "ckgmnr" and faocwk[-2] != "vwx"
def is_eargi_tdypks(faocwk):
    return not is_eargi_xmehrd(faocwk)
eargi = Factor("eargi", [DerivedLevel("xmehrd", Window(is_eargi_xmehrd, [faocwk], 3, 1)), DerivedLevel("tdypks", Window(is_eargi_tdypks, [faocwk], 3, 1))])

design=[faocwk,eargi]
crossing=[eargi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END