from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hstuwb = Factor("hstuwb", ["leuc","epe","vtgmh","grktu","lzciwx","slzolh"])
zfln = Factor("zfln", ["ydiyqj","nhj","rld","llh","dnsu","qiwv"])
def is_eqm_fbhrc(hstuwb, zfln):
    return hstuwb[-1] == "slzolh" and zfln[0] != "ydiyqj"
def is_eqm_thwl(hstuwb, zfln):
    return hstuwb[-1] != "slzolh" and zfln[0] == "ydiyqj"
def is_eqm_ixo(hstuwb, zfln):
    return not (is_eqm_fbhrc(hstuwb, zfln) or is_eqm_thwl(hstuwb, zfln))
eqm = Factor("eqm", [DerivedLevel("fbhrc", Transition(is_eqm_fbhrc, [hstuwb, zfln])), DerivedLevel("thwl", Transition(is_eqm_thwl, [hstuwb, zfln])), DerivedLevel("ixo", Transition(is_eqm_ixo, [hstuwb, zfln]))])

design=[hstuwb,zfln,eqm]
crossing=[eqm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END