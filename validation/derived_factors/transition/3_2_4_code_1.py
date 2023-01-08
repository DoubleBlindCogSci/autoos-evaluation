from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
blorw = Factor("blorw", ["xkag","hyvlqh","vjh","txlvm","pexht","qef"])
aqsrs = Factor("aqsrs", ["dhil","wvzi","xsgh","sosn","cmyn","dhjkgj"])
def htau(blorw, aqsrs):
     return "vjh" == blorw[-1] and not aqsrs[0] == "xsgh"
def sjajnv(blorw, aqsrs):
     return blorw[-1] != "vjh" and aqsrs[0] == "xsgh"
def yzxb(blorw, aqsrs):
     return (not blorw[-1] == "vjh") and (not aqsrs[0] == "xsgh")
gln = Factor("uih", [DerivedLevel("mpk", Transition(htau, [blorw, aqsrs])), DerivedLevel("ihdfm", Transition(sjajnv, [blorw, aqsrs])),DerivedLevel("rjozpb", Transition(yzxb, [blorw, aqsrs]))])
### EXPERIMENT
design=[blorw,aqsrs,gln]
crossing=[gln]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END