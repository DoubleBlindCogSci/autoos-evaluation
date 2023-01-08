from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mjsmfy= Factor("mjsmfy", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
uubtu= Factor("uubtu", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
jqdmb= Factor("jqdmb", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
def is_lxcta_wql(jqdmb, mjsmfy):
    return jqdmb[0] == mjsmfy[-2]
def is_lxcta_byxd(jqdmb, mjsmfy, uubtu):
    return jqdmb[0] != mjsmfy[-2] and mjsmfy[0] == uubtu[-2]
def is_lxcta_rnzv(jqdmb, mjsmfy, uubtu):
    return jqdmb[0] != mjsmfy[-2] and mjsmfy[0] != uubtu[-2]
lxcta= Factor("lxcta", [DerivedLevel("wql", Window(is_lxcta_wql, [jqdmb, mjsmfy], 3, 1)), DerivedLevel("byxd", Window(is_lxcta_byxd, [jqdmb, mjsmfy, uubtu], 3, 1)), DerivedLevel("rnzv", Window(is_lxcta_rnzv, [jqdmb, mjsmfy, uubtu], 3, 1))])

design=[mjsmfy,uubtu,jqdmb,lxcta]
crossing=[lxcta]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
