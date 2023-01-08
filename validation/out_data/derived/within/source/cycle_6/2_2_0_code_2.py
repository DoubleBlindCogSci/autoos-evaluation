from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oxwelr = Factor("oxwelr", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
jvns = Factor("jvns", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
swkxs = Factor("swkxs", ["nrxuec","exzhpx","bvfan","cazaj","idwx"])
def is_bpso_bzvnpz(oxwelr, jvns, swkxs):
    return oxwelr != swkxs
def is_bpso_trjlm(oxwelr, jvns, swkxs):
    return not is_bpso_bzvnpz(oxwelr, jvns, swkxs)
bpso = Factor("bpso", [DerivedLevel("bzvnpz", WithinTrial(is_bpso_bzvnpz, [oxwelr, jvns, swkxs])), DerivedLevel("trjlm", WithinTrial(is_bpso_trjlm, [oxwelr, jvns, swkxs]))])

design=[oxwelr,jvns,swkxs,bpso]
crossing=[bpso]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END