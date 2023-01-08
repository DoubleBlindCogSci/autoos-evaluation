from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oxwelr = Factor("oxwelr", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
jvns = Factor("jvns", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
swkxs = Factor("swkxs", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
def yjsjui(oxwelr, swkxs, jvns):
    return oxwelr != swkxs
def riikv(oxwelr, swkxs, jvns):
    return not (oxwelr != swkxs)
zodsp = Factor("bpso", [DerivedLevel("bzvnpz", WithinTrial(yjsjui, [oxwelr, jvns, swkxs])), DerivedLevel("trjlm", WithinTrial(riikv, [oxwelr, jvns, swkxs]))])
### EXPERIMENT
design=[oxwelr,jvns,swkxs,zodsp]
crossing=[zodsp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END