from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hibrnw = Factor("hibrnw", ["ggih","hdhoy","blomac","waxo","zjy","yijm","jphvzw","ouebqa"])
def aamy(hibrnw):
     return hibrnw[0] == "blomac" and not hibrnw[-1] == "hdhoy"
def mmn(hibrnw):
     return (not "blomac" != hibrnw[0]) and  hibrnw[-1] == "hdhoy"
def ibf(hibrnw):
     return (hibrnw[0] != "blomac") and (not mmn(hibrnw))
nndtn = Factor("norzp", [DerivedLevel("ysu", Transition(aamy, [hibrnw])), DerivedLevel("ovfnl", Transition(mmn, [hibrnw])),DerivedLevel("nfyhcz", Transition(ibf, [hibrnw]))])
### EXPERIMENT
design=[hibrnw,nndtn]
crossing=[nndtn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END