from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mjsmfy = Factor("mjsmfy", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
uubtu = Factor("uubtu", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
jqdmb = Factor("jqdmb", ["zpc","lehda","nrfcn","hfb","hkva","hdzaoo"])
def jgw(mjsmfy, jqdmb, uubtu):
     return jqdmb[-1] == mjsmfy[-2]
def osjtug(mjsmfy, jqdmb, uubtu):
     return jqdmb[-1] != mjsmfy[-2] and mjsmfy[-1] == uubtu[-2]
def rqtw(mjsmfy, jqdmb, uubtu):
     return (not mjsmfy[-2] == jqdmb[-1]) and (mjsmfy[-1] != uubtu[-2])
bdq = Factor("lxcta", [DerivedLevel("wql", Window(jgw, [mjsmfy, uubtu, jqdmb],3,1)), DerivedLevel("byxd", Window(osjtug, [mjsmfy, uubtu, jqdmb],3,1)),DerivedLevel("rnzv", Window(rqtw, [mjsmfy, uubtu, jqdmb],3,1))])
### EXPERIMENT
design=[mjsmfy,uubtu,jqdmb,bdq]
crossing=[bdq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END