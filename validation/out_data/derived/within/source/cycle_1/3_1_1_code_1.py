from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pbbncw = Factor("pbbncw", ["nmxpb","itt","ijv","imuzj","tjfdht","eumhf","mravi"])
def mddw(pbbncw):
     return pbbncw == "nmxpb"
def lwn(pbbncw):
     return "mravi" == pbbncw
def iuar(pbbncw):
     return (not mddw(pbbncw)) and (not lwn(pbbncw))
rsbjw = Factor("jwgl", [DerivedLevel("yzl", WithinTrial(mddw, [pbbncw])), DerivedLevel("qvxiuo", WithinTrial(lwn, [pbbncw])),DerivedLevel("mqi", WithinTrial(iuar, [pbbncw]))])
### EXPERIMENT
design=[pbbncw,rsbjw]
crossing=[rsbjw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END