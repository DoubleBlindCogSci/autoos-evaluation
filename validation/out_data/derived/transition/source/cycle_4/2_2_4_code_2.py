from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mdl = Factor("mdl", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
xxksa = Factor("xxksa", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
ofn = Factor("ofn", ["fifp","xqe","rlt","ceicfs","xyzxyd","dtj","ypplxv"])
def is_khgdqa_ursslu(mdl, xxksa, ofn):
    return mdl[0] == xxksa[-1]
def is_khgdqa_bxa(mdl, xxksa, ofn):
    return not is_khgdqa_ursslu(mdl, xxksa, ofn)
khgdqa = Factor("khgdqa", [DerivedLevel("ursslu", Transition(is_khgdqa_ursslu, [mdl, xxksa, ofn])), DerivedLevel("bxa", Transition(is_khgdqa_bxa, [mdl, xxksa, ofn]))])

design=[mdl,xxksa,ofn,khgdqa]
crossing=[khgdqa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END