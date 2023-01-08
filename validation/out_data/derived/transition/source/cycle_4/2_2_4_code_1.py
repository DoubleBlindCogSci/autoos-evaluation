from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mdl = Factor("mdl", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
xxksa = Factor("xxksa", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
ofn = Factor("ofn", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
def srrzs(mdl, xxksa, ofn):
    return mdl[0] == xxksa[-1]
def cmwdc(mdl, xxksa, ofn):
    return not srrzs(mdl, xxksa, ofn)
pcxcv = Factor("khgdqa", [DerivedLevel("ursslu", Transition(srrzs, [mdl, xxksa, ofn])), DerivedLevel("bxa", Transition(cmwdc, [mdl, xxksa, ofn]))])
### EXPERIMENT
design=[mdl,xxksa,ofn,pcxcv]
crossing=[pcxcv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END