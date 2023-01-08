from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nuh = Factor("nuh", ["jtv","gvgvz","ysog","fzejv","kedcat","zuefq","wwfptp"])
srcbv = Factor("srcbv", ["kizoj","xgiimi","pvqs","mok","rnzppo","pxnav","ugutef"])
def is_mnjfm_egilme(nuh, srcbv):
    return nuh == "zuefq"
def is_mnjfm_oxv(nuh, srcbv):
    return nuh != "zuefq" and srcbv == "pxnav"
def is_mnjfm_qqmd(nuh, srcbv):
    return not (is_mnjfm_egilme(nuh, srcbv) or is_mnjfm_oxv(nuh, srcbv))
mnjfm= Factor("mnjfm", [DerivedLevel("egilme", WithinTrial(is_mnjfm_egilme, [nuh, srcbv])), DerivedLevel("oxv", WithinTrial(is_mnjfm_oxv, [nuh, srcbv])), DerivedLevel("qqmd", WithinTrial(is_mnjfm_qqmd, [nuh, srcbv]))])

design=[nuh,srcbv,mnjfm]
crossing=[mnjfm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
