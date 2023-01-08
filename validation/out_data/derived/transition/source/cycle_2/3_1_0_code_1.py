from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nzeyhy = Factor("nzeyhy", ["qyl","vnxtdl","tjy","mvbc","lvo","gbxcg"])
def grv(nzeyhy):
     return nzeyhy[0] == "gbxcg" and not nzeyhy[-1] == "lvo"
def pdcb(nzeyhy):
     return (nzeyhy[0] != "gbxcg") and  nzeyhy[-1] == "lvo"
def hynib(nzeyhy):
     return (nzeyhy[0] != "gbxcg") and (nzeyhy[-1] != "lvo")
rbyqi = Factor("umf", [DerivedLevel("olado", Transition(grv, [nzeyhy])), DerivedLevel("dxkmeo", Transition(pdcb, [nzeyhy])),DerivedLevel("yedcyl", Transition(hynib, [nzeyhy]))])
### EXPERIMENT
design=[nzeyhy,rbyqi]
crossing=[rbyqi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END