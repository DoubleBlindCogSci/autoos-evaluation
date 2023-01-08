from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nqqiy = Factor("nqqiy", ["eeqbsh","sae","rkko","evem","wgk","paiya"])
def is_qxlo_dnoth(nqqiy):
    return nqqiy != "evem"
def is_qxlo_ckgzws(nqqiy):
    return not is_qxlo_dnoth(nqqiy)
qxlo = Factor("qxlo", [DerivedLevel("dnoth", WithinTrial(is_qxlo_dnoth, [nqqiy])), DerivedLevel("ckgzws", WithinTrial(is_qxlo_ckgzws, [nqqiy]))])

design=[nqqiy,qxlo]
crossing=[qxlo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END