from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hibrnw = Factor("hibrnw", ["ggih","hdhoy","blomac","waxo","zjy","yijm","jphvzw","ouebqa"])
def is_norzp_ysu(hibrnw):
    return hibrnw[0] == "blomac" and hibrnw[-1] != "hdhoy"
def is_norzp_ovfnl(hibrnw):
    return hibrnw[0] == "hdhoy" and hibrnw[-1] == "blomac"
def is_norzp_nfyhcz(hibrnw):
    return hibrnw[0] != "blomac" and hibrnw[-1] != "hdhoy"
norzp = Factor("norzp", [DerivedLevel("ysu", Transition(is_norzp_ysu, [hibrnw])), DerivedLevel("ovfnl", Transition(is_norzp_ovfnl, [hibrnw])), DerivedLevel("nfyhcz", Transition(is_norzp_nfyhcz, [hibrnw]))])

design=[hibrnw,norzp]
crossing=[norzp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END