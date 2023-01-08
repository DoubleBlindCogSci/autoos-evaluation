from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
molokf = Factor("molokf", ["zihb","ffmhv","pyklyv","etbiy","xhrx"])
ooyt = Factor("ooyt", ["hlhdjb","hhd","vaq","rdv","hoin","qte","opv"])
def is_mod_lgdc(molokf, ooyt):
    return molokf[-3] == "zihb" and ooyt[-2] != "hoin"
def is_mod_pmkjr(molokf, ooyt):
    return not is_mod_lgdc(molokf, ooyt)
mod = Factor("mod", [DerivedLevel("lgdc", Window(is_mod_lgdc, [molokf, ooyt], 4, 1)), DerivedLevel("pmkjr", Window(is_mod_pmkjr, [molokf, ooyt], 4, 1))])

design=[molokf,ooyt,mod]
crossing=[mod]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END