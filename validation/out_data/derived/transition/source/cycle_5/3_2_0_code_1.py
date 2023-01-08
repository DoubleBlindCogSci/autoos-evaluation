from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
etbwc = Factor("etbwc", ["vng","lrcjcy","otkqu","lih","lql","kic","evkwk"])
xpzx = Factor("xpzx", ["rwa","wmkbw","drfacm","zuhuen","tlxb","kdoe","dgtt"])
def ccwlc(etbwc, xpzx):
     return "otkqu" == etbwc[-1] and xpzx[0] != "drfacm"
def fsvh(etbwc, xpzx):
     return "otkqu" != etbwc[-1] and xpzx[0] == "drfacm"
def ontyq(etbwc, xpzx):
     return (not etbwc[-1] == "otkqu") and (xpzx[0] != "drfacm")
tej = Factor("itt", [DerivedLevel("mhi", Transition(ccwlc, [etbwc, xpzx])), DerivedLevel("zjkjh", Transition(fsvh, [etbwc, xpzx])),DerivedLevel("mktwdr", Transition(ontyq, [etbwc, xpzx]))])
### EXPERIMENT
design=[etbwc,xpzx,tej]
crossing=[tej]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END