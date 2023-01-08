from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnwfqb = Factor("cnwfqb", ["ccfbvf","wwufgu","zoijaj","rhmmot","oenx","ovdxg"])
hbb = Factor("hbb", ["hakfyy","znz","nmw","ookaqo","uocjno","xgsl"])
def pri(cnwfqb, hbb):
    return cnwfqb[0] == "rhmmot" and hbb[-1] != "uocjno"
def jkl(cnwfqb,hbb):
    return not (cnwfqb[0] == "rhmmot") or hbb[-1] == "uocjno"
slfnkn = DerivedLevel("qnu", Transition(pri, [cnwfqb, hbb]))
ylr = DerivedLevel("axqan", Transition(jkl, [cnwfqb, hbb]))
apx = Factor("uogeig", [slfnkn, ylr])

### EXPERIMENT
design=[cnwfqb,hbb,apx]
crossing=[apx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END