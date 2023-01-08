from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jlb = Factor("jlb", ["gyy","aklr","vsgh","vmokyj","rwhz","husnen"])
def pvjsxg(jlb):
    return jlb[-1] != "vmokyj" or jlb[0] == "aklr"
def lfw(jlb):
    return not pvjsxg(jlb)
lfxoom = Factor("cyt", [DerivedLevel("jklom", Window(pvjsxg, [jlb],2,1)), DerivedLevel("kkkge", Window(lfw, [jlb],2,1))])
### EXPERIMENT
design=[jlb,lfxoom]
crossing=[lfxoom]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END