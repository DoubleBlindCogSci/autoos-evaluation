from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cnwfqb = Factor("cnwfqb", ["ccfbvf","wwufgu","zoijaj","rhmmot","oenx","ovdxg"])
hbb = Factor("hbb", ["hakfyy","znz","nmw","ookaqo","uocjno","xgsl"])
def is_uogeig_qnu(cnwfqb, hbb):
    return cnwfqb[0] == "rhmmot" and hbb[-1] != "uocjno"
def is_uogeig_axqan(cnwfqb, hbb):
    return not is_uogeig_qnu(cnwfqb, hbb)
uogeig = Factor("uogeig", [DerivedLevel("qnu", Transition(is_uogeig_qnu, [cnwfqb, hbb])), DerivedLevel("axqan", Transition(is_uogeig_axqan, [cnwfqb, hbb]))])

design=[cnwfqb,hbb,uogeig]
crossing=[uogeig]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END